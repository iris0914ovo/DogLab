"""Independent final remote and local verification for 120 actual full-body PNGs."""
from pathlib import Path
from datetime import datetime,timezone
from PIL import Image,ImageFilter
import numpy as np
import subprocess,hashlib,json,io
from illustration_batch import ROOT,catalog,sha

def verify():
 q=json.loads((ROOT/'docs/asset-production/round3-queue.json').read_text());assert len(q['tasks'])==102 and all(t['status']=='synced' for t in q['tasks'])
 records=[json.loads(f.read_text()) for f in (ROOT/'docs/asset-production/records').glob('B*-full-*.json') if json.loads(f.read_text()).get('is_current',True)]
 assert len(records)==120 and {r['breed_id'] for r in records}==set(catalog())
 assert len({r['sha256'] for r in records})==120 and len({r['pixels_sha256'] for r in records})==120
 assert len(list((ROOT/'public/assets/dogs/full').glob('*.png')))==120
 assert not list((ROOT/'public/assets/dogs/portrait').glob('*.png'))
 prior=json.loads((ROOT/'docs/asset-production/round3-preserved-assets.json').read_text())
 for path,h in prior.items():assert sha(ROOT/path)==h
 for r in records:
  assert r['slug']==catalog()[r['breed_id']][3]
  assert r['path']==f"public/assets/dogs/full/{r['slug']}-full.png"
  for path,h in [(r['path'],r['sha256']),(r['raw_path'],r['raw_sha256']),(r['prompt_path'],r['prompt_sha256'])]:assert sha(ROOT/path)==h
  im=Image.open(ROOT/r['path']);im.load();assert im.mode=='RGBA' and im.format=='PNG' and im.size==(1024,1024)
  a=np.array(im.getchannel('A'));box=im.getchannel('A').getbbox();assert a.min()==0 and a.max()==255 and ((a>0)&(a<255)).any()
  assert min(box[0],box[1],1024-box[2],1024-box[3])>=102
  core=np.array(im.getchannel('A').point(lambda x:255 if x>128 else 0).filter(ImageFilter.MinFilter(9)))==255;assert (a[core]==255).all()
 # Compare unchanged product documents to the pre-round3 commit.
 for name in ['PRD','QUESTION_BANK','PERSONALITY_DATA','BREED_DATA','CONTENT_GUIDELINES','DESIGN_SYSTEM']:
  path=f'docs/{name}.md';assert (ROOT/path).read_bytes()==subprocess.check_output(['git','show',f'7e151c0:{path}'],cwd=ROOT)
 origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=ROOT,text=True).strip();assert origin=='https://github.com/iris0914ovo/DogLab.git'
 head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
 refs=dict((l.split()[1],l.split()[0]) for l in subprocess.check_output(['git','ls-remote','origin','refs/heads/work','refs/heads/main'],cwd=ROOT,text=True).splitlines())
 assert refs['refs/heads/work']==head and refs['refs/heads/main']=='e885330cda4018c7ac216eeb4351a947fbd65284'
 d='/tmp/doglab-round3-remote-verification';subprocess.run(['git','-C',d,'fetch','--quiet','--depth=1',origin,'work'],check=True)
 remote_files=[]
 for r in records:
  data=subprocess.check_output(['git','-C',d,'show','FETCH_HEAD:'+r['path']]);assert hashlib.sha256(data).hexdigest()==r['sha256']
  im=Image.open(io.BytesIO(data));im.load();assert im.mode=='RGBA' and im.size==(1024,1024) and im.getchannel('A').getextrema()==(0,255)
  remote_files.append(dict(breed_id=r['breed_id'],path=r['path'],sha256=r['sha256'],bytes=len(data)))
 proofs=[]
 for batch in dict.fromkeys(t['batch_id'] for t in q['tasks']):
  v=json.loads((ROOT/f'docs/asset-production/verification/{batch}.json').read_text());assert v['success'];proofs.append(dict(batch_id=batch,production_commit=v['production_commit']))
 assert len(proofs)==9
 result=dict(checked_at=datetime.now(timezone.utc).isoformat(),success=True,branch='work',production_head=head,main_unchanged=True,total_current_full_body_png=120,round3_completed=102,batches=proofs,generation_attempts=sum(t.get('generation_attempts',1) for t in q['tasks']),retry_breeds=[dict(breed_id=t['id'],attempts=t.get('generation_attempts',1),version=t.get('version','v01')) for t in q['tasks'] if t.get('generation_attempts',1)>1],failed_current_outputs=[],preserved_prior_png_count=len(prior),portraits=0,method='Independent remote Git object repository; all 120 PNG remote blobs decoded and SHA256 checked, plus local core alpha/margins/provenance checks',files=remote_files)
 (ROOT/'docs/asset-production/verification/round3-final-120.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['success','total_current_full_body_png','round3_completed','generation_attempts','retry_breeds','preserved_prior_png_count','portraits','production_head']},ensure_ascii=False))
if __name__=='__main__':verify()
