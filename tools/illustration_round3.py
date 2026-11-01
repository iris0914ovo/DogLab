"""Round3 checkpoint, QC, contact sheets and independent Git verification.
Generation uses the current session image tool, never an independent paid API.
"""
from pathlib import Path
from datetime import datetime,timezone
from PIL import Image,ImageDraw,ImageFont
import sys,json,re,hashlib,subprocess,tempfile,io,itertools
import numpy as np
import illustration_batch as base
ROOT=base.ROOT;QPATH=ROOT/'docs/asset-production/round3-queue.json'
def queue():return json.loads(QPATH.read_text())
def saveq(q):
 temp=QPATH.with_suffix('.tmp');temp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n');temp.replace(QPATH)
def ingest(id,source):
 q=queue();t=next(t for t in q['tasks'] if t['id']==id)
 base.IDS=[t['id'] for t in q['tasks']];base.BATCH=t['batch_id'];base.VERSION='v01';base.STYLE='DPL-ILL-1.2'
 base.ingest(id,source)
 path=ROOT/f'docs/asset-production/records/{id}-full-v01.json';r=json.loads(path.read_text())
 ref='public/assets/dogs/review/round2-dpl-ill-1.2-v01-paper.png'
 r['reference_images']=[dict(path=ref,sha256=base.sha(ROOT/ref),scope='User-approved round2 style; not copied anatomy')]
 r['tool_parameters']=dict(transparent_background=True,referenced_image_paths=[str(ROOT/ref)])
 r['breed_profile']=t['profile'];r['qc']['visual_status']='NEEDS_AI_AND_USER_REVIEW'
 r['qc']['source_alpha_touches_canvas']=any([r['raw_qc']['bbox'][0]==0,r['raw_qc']['bbox'][1]==0,r['raw_qc']['bbox'][2]==r['raw_qc']['size'][0],r['raw_qc']['bbox'][3]==r['raw_qc']['size'][1]])
 path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 t.update(status='qc_pass' if r['qc']['technical_pass'] else 'qc_fail',record_path=str(path.relative_to(ROOT)),source_path=source)
 saveq(q)
 if not r['qc']['technical_pass']:raise RuntimeError('Real output saved but technical QC failed; retry processing only')
def finalize(batch):
 q=queue();tasks=[t for t in q['tasks'] if t['batch_id']==batch];assert 10<=len(tasks)<=12
 records=[]
 for t in tasks:
  assert t['status'] in ['qc_pass','synced'];r=json.loads((ROOT/t['record_path']).read_text());assert base.sha(ROOT/r['path'])==r['sha256'];records.append(r)
 allr=[json.loads(f.read_text()) for f in (ROOT/'docs/asset-production/records').glob('B*-full-*.json')]
 assert len({r['sha256'] for r in allr})==len(allr),'Duplicate final binary'
 assert len({r['pixels_sha256'] for r in allr})==len(allr),'Duplicate image pixels'
 prior=json.loads((ROOT/'docs/asset-production/round3-preserved-assets.json').read_text())
 for path,h in prior.items():assert base.sha(ROOT/path)==h,'Prior image changed'
 hashes={}
 for r in allr:
  a=np.array(Image.open(ROOT/r['path']).getchannel('A').resize((8,8),Image.Resampling.BOX));hashes[r['breed_id']]=a>a.mean()
 near=[];ids={r['breed_id'] for r in records}
 for (a,ha),(b,hb) in itertools.combinations(hashes.items(),2):
  dist=int((ha!=hb).sum())
  if dist<8 and (a in ids or b in ids):near.append(dict(ids=[a,b],hamming=dist,note='Silhouette warning; not proof of duplication; requires AI/user visual review'))
 font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',21);small=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',17)
 contacts=[]
 for label,bg,fg in [('paper','#F5F0E6','#20201D'),('ink','#20201D','#F5F0E6')]:
  sheet=Image.new('RGB',(2048,1740),bg);draw=ImageDraw.Draw(sheet)
  for i,r in enumerate(records):
   x=i%4*512;y=i//4*580;im=Image.open(ROOT/r['path']).convert('RGBA').resize((480,480),Image.Resampling.LANCZOS);sheet.paste(im,(x+16,y+8),im)
   draw.text((x+18,y+492),f"{r['breed_id']} {r['name']}",font=font,fill=fg)
   draw.text((x+18,y+534),'DPL-ILL-1.2 | v01 | 人工待审核',font=small,fill=fg)
  path=ROOT/f'public/assets/dogs/review/{batch}-{label}.png'
  if path.exists():
   import io
   buf=io.BytesIO();sheet.save(buf,format='PNG');assert path.read_bytes()==buf.getvalue(),'Do not overwrite prior contact sheet'
  else:sheet.save(path)
  contacts.append(str(path.relative_to(ROOT)))
 result=dict(batch_id=batch,breed_ids=[r['breed_id'] for r in records],record_paths=[t['record_path'] for t in tasks],contact_sheets=contacts,technical_pass_count=len(records),failed_ids=[],exact_duplicates=False,near_silhouette_warnings=near,human_review_status='PLANNED',style_version='DPL-ILL-1.2',scope='Full-body only; no portraits or website')
 (ROOT/f'docs/asset-production/batches/{batch}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 update_manifest(allr)
 report=f'# {batch} 生产与基础质检报告\n\n实际独立生成并保存{len(records)}张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。\n\n跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号{len(near)}项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。\n\n|ID|犬种|PNG|记录|基础QC|\n|---|---|---|---|---|\n'
 for t,r in zip(tasks,records):report+=f"|{r['breed_id']}|{r['name']}|[PNG](../../{r['path']})|[JSON](records/{r['breed_id']}-full-v01.json)|PASS|\n"
 for c in contacts:report+=f'\n[合版 {Path(c).stem}](../../{c})\n'
 report+='\n每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。\n'
 (ROOT/f'docs/asset-production/{batch}-REPORT.md').write_text(report)
 print(json.dumps(dict(batch=batch,count=len(records),contacts=contacts,near_signals=len(near)),ensure_ascii=False))
def update_manifest(allr):
 p=ROOT/'docs/ASSET_MANIFEST.md';s=p.read_text();lines=[];byid={r['breed_id']:r for r in allr}
 for line in s.splitlines():
  if re.match(r'^\| B\d{3} \|',line):
   row=line.strip('| ').split(' | ');r=byid.get(row[0])
   if r:
    approved=r['human_review_status']=='APPROVED'
    row[7]='PLANNED' if row[4]=='是' else 'GENERATED';row[8]='PLANNED' if row[4]=='是' or not approved else 'APPROVED'
    row[9]=('全身 APPROVED：' if approved else '全身 GENERATED：')+r['path']+('；肖像未制作' if row[4]=='是' else '')
    if not approved:row[10]='第三轮基础技术QC通过；犬种形态、相似性与画风待AI批次检视及最终人工复核。'
   line='| '+' | '.join(row)+' |'
  lines.append(line)
 s='\n'.join(lines)+'\n';a=s.index('来源：');b=s.index('## 状态约定')
 s=s[:a]+f'来源：BREED_DATA的120条唯一记录。当前{len(allr)}张全身PNG实际落库；前两轮18张已获用户审核通过，第三轮已生成{len(allr)-18}/102张，仍待最终人工复核。32张肖像均未制作。正式人格按所需资产最低进度聚合，肖像缺席时为PLANNED；已生成全身文件在实际文件栏和逐图记录明确列出，不重复生产。\n\n'+s[b:]
 if '\n共18张实际全身PNG' in s:s=s[:s.index('\n共18张实际全身PNG')]
 marker='\n第三轮进度：'
 if marker in s:s=s[:s.index(marker)]
 s+=f'\n第三轮进度：已落库{len(allr)-18}/102，DPL-ILL-1.2；每批合版、报告和独立验证记录见 docs/asset-production/。第三轮不自动标人工批准；既有18张PNG受哈希保护，不生产肖像、网站或部署。\n';p.write_text(s)
def sync(batch):
 assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='work'
 origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=ROOT,text=True).strip();assert origin=='https://github.com/iris0914ovo/DogLab.git'
 q=queue();tasks=[t for t in q['tasks'] if t['batch_id']==batch]
 # Explicit scope includes queued prompt text but never fake future PNGs.
 paths=['docs/ILLUSTRATION_GUIDE.md','docs/ILLUSTRATION_REVIEW.md','docs/ASSET_MANIFEST.md','docs/asset-production','artifacts/illustrations','tools/illustration_round3.py','README.md','public/assets/dogs/full','public/assets/dogs/review']
 subprocess.run(['git','add','--',*paths],cwd=ROOT,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,check=True)
 subprocess.run(['git','commit','-m',f'art: produce {batch}'],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
 head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
 subprocess.run(['git','push','origin','work'],cwd=ROOT,check=True)
 refs=dict((l.split()[1],l.split()[0]) for l in subprocess.check_output(['git','ls-remote','origin','refs/heads/work','refs/heads/main'],cwd=ROOT,text=True).splitlines())
 assert refs['refs/heads/work']==head and refs['refs/heads/main']=='e885330cda4018c7ac216eeb4351a947fbd65284'
 b=json.loads((ROOT/f'docs/asset-production/batches/{batch}.json').read_text());verified=[]
 with __import__('contextlib').nullcontext('/tmp/doglab-round3-remote-verification') as d:
  subprocess.run(['git','init','--bare','-q',d],check=True);subprocess.run(['git','-C',d,'fetch','--quiet','--depth=1',origin,'work'],check=True)
  def get(path):return subprocess.check_output(['git','-C',d,'show','FETCH_HEAD:'+path])
  for path in b['record_paths']:
   blob=get(path);assert hashlib.sha256(blob).hexdigest()==base.sha(ROOT/path);r=json.loads(blob)
   for k,h in [('path','sha256'),('raw_path','raw_sha256'),('prompt_path','prompt_sha256')]:
    data=get(r[k]);assert hashlib.sha256(data).hexdigest()==r[h]
    if k=='path':
     im=Image.open(io.BytesIO(data));im.load();assert im.size==(1024,1024) and im.mode=='RGBA' and im.getchannel('A').getextrema()==(0,255)
    verified.append(dict(path=r[k],sha256=r[h],bytes=len(data)))
  for path in b['contact_sheets']:
   data=get(path);assert hashlib.sha256(data).hexdigest()==base.sha(ROOT/path);verified.append(dict(path=path,sha256=base.sha(ROOT/path)))
 result=dict(batch_id=batch,production_commit=head,checked_at=datetime.now(timezone.utc).isoformat(),success=True,method='Independent temporary Git repository fetch, actual remote blob SHA256/PNG decode',files=verified,main_unchanged=True)
 (ROOT/f'docs/asset-production/verification/{batch}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 for t in q['tasks']:
  if t['batch_id']==batch:t.update(status='synced',production_commit=head)
 saveq(q)
 print(json.dumps(dict(batch=batch,commit=head,remote_files_verified=len(verified)),ensure_ascii=False))
if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='ingest':ingest(sys.argv[2],sys.argv[3])
 elif mode=='finalize':finalize(sys.argv[2])
 elif mode=='sync':sync(sys.argv[2])
 else:raise SystemExit('Unknown mode')
