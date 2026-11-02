"""DPL-DOODLE-1.0 batch01 ingestion, QC, review sheets and version manifest.
No generation API calls. python3 tools/doodle_batch.py ingest B006 /tool/output.png
python3 tools/doodle_batch.py finalize
"""
from pathlib import Path
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import json,hashlib,shutil,sys
import numpy as np
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
DOC=R/'docs/asset-production/doodle';OUT=R/'public/assets/dogs/doodle-v01'
PLAN=json.loads((DOC/'batch01/plan.json').read_text())
CAT=json.loads((DOC/'catalog.json').read_text())
BASE=json.loads((R/'public/assets/dogs/style-tests/doodle-v01/manifest.json').read_text())['records']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return str(p.relative_to(R))
def write(p,obj):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def metrics(im):
 a=np.array(im.getchannel('A'));bb=im.getchannel('A').getbbox();assert bb
 core=np.array(im.getchannel('A').point(lambda v:255 if v>128 else 0).filter(ImageFilter.MinFilter(9)))==255
 margins=[bb[0],bb[1],1024-bb[2],1024-bb[3]]
 q=dict(size=list(im.size),mode=im.mode,bbox=list(bb),margins=margins,alpha_min=int(a.min()),alpha_max=int(a.max()),transparent_pixels=int((a==0).sum()),opaque_pixels=int((a==255).sum()),partial_alpha_pixels=int(((a>0)&(a<255)).sum()),translucent_core_pixels=int(((a<255)&core).sum()))
 q['checks']=dict(size=im.size==(1024,1024),rgba=im.mode=='RGBA',real_transparency=q['transparent_pixels']>0 and q['opaque_pixels']>0,safe_margin=min(margins)>=100,opaque_core=q['translucent_core_pixels']==0,antialias=q['partial_alpha_pixels']>0)
 q['technical_pass']=all(q['checks'].values());return q
REFS=[R/'public/assets/dogs/style-tests/doodle-v01'/f'{s}-full.png' for s in ['shiba-inu','golden-retriever','border-collie']]
def ingest(id,source,version="v01"):
 row=next(x for x in PLAN if x['id']==id);src=Path(source)
 raw=R/f'artifacts/illustrations/doodle-v01/batch01/{id}/{"raw.png" if version=="v01" else "raw-"+version+".png"}';raw.parent.mkdir(parents=True,exist_ok=True)
 if raw.exists():assert sha(raw)==sha(src)
 else:shutil.copyfile(src,raw)
 record=DOC/f'batch01/{id}/record.json';dst=OUT/f'{id}-full.png'
 if record.exists():assert sha(dst)==json.loads(record.read_text())['sha256'];print(id,'already ingested');return
 assert not dst.exists()
 with Image.open(raw) as im:
  assert im.format=='PNG' and im.mode=='RGBA';im.load();source=im.copy()
 a=np.array(source.getchannel('A'));assert (a==0).sum()>0 and (a>=250).sum()>0
 a[a<=2]=0;source.putalpha(Image.fromarray(a));box=source.getchannel('A').getbbox();assert box
 crop=source.crop(box);scale=816/max(crop.size);size=tuple(round(d*scale) for d in crop.size);crop=crop.resize(size,Image.Resampling.LANCZOS)
 a=np.array(crop.getchannel('A'));a[a<=2]=0;core=np.array(Image.fromarray((a>128).astype('uint8')*255).filter(ImageFilter.MinFilter(9)))==255
 a[core]=255;a[a>=250]=255;crop.putalpha(Image.fromarray(a))
 canvas=Image.new('RGBA',(1024,1024),(0,0,0,0));pos=((1024-size[0])//2,(1024-size[1])//2);canvas.paste(crop,pos)
 with dst.open('xb') as f:canvas.save(f,format='PNG')
 with Image.open(dst) as check:check.load();q=metrics(check)
 assert q['technical_pass'],q
 prompt=DOC/f'batch01/{id}/prompt.txt'
 record_data=dict(id=id,name=row['name'],english=row['english'],slug=row['slug'],style='DPL-DOODLE-1.0',batch='batch01',production_status='GENERATED',human_review_status='PENDING_REVIEW',saved_at_utc=datetime.now(timezone.utc).isoformat(),tool='image_gen__imagegen',model_id=None,seed=None,tool_source_path=str(src),references=[dict(path=rel(p),sha256=sha(p)) for p in ([R/'artifacts/illustrations/doodle-v01/batch01/B010/candidate-v01.png',*REFS[:2]] if version=='v02' else REFS)],generation_version=version,design=row['design'],raw_path=rel(raw),raw_sha256=sha(raw),raw_size=list(source.size),prompt_path=rel(prompt),prompt_sha256=sha(prompt),path=rel(dst),sha256=sha(dst),pixels_sha256=hashlib.sha256(canvas.tobytes()).hexdigest(),processing=dict(bbox=list(box),scale=scale,resized_dimensions=list(size),position=list(pos),alpha='<=2 to0; eroded interior and >=250 to255; preserve edge AA; raw retained'),qc=q)
 write(record,record_data);print(id,'QC PASS',sha(dst))
def finalize():
 records=[json.loads((DOC/f'batch01/{p["id"]}/record.json').read_text()) for p in PLAN]
 assert len(records)==12 and len({r['sha256'] for r in records})==12 and len({r['pixels_sha256'] for r in records})==12
 for r in records:assert sha(R/r['path'])==r['sha256'] and r['qc']['technical_pass']
 font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',22);small=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',16)
 review=OUT/'review';review.mkdir(exist_ok=True)
 for theme,bg,fg in [('paper','#F5F0E6','#20201D'),('ink','#20201D','#F5F0E6')]:
  sheet=Image.new('RGB',(1920,1656),bg);draw=ImageDraw.Draw(sheet)
  for i,r in enumerate(records):
   x=i%4*480;y=i//4*552;im=Image.open(R/r['path']).resize((480,480),Image.Resampling.LANCZOS);sheet.paste(im,(x,y),im)
   draw.text((x+18,y+480),r['id']+' '+r['name'],font=font,fill=fg);draw.text((x+18,y+520),'DPL-DOODLE-1.0 / 待人工审核',font=small,fill=fg)
  sheet.save(review/f'batch01-{theme}.png')
 sheet=Image.new('RGB',(1024,576),'#F5F0E6');draw=ImageDraw.Draw(sheet)
 for i,r in enumerate(records):
  x=i%4*256;y=i//4*192
  for sz,offset in [(128,0),(64,144)]:
   im=Image.open(R/r['path']).resize((sz,sz),Image.Resampling.LANCZOS);sheet.paste(im,(x+offset,y),im)
  draw.text((x+8,y+140),r['id']+' 128px / 64px',font=small,fill='#20201D')
 sheet.save(review/'batch01-thumbnails.png')
 write(DOC/'batch01/manifest.json',dict(style='DPL-DOODLE-1.0',status='GENERATED',human_review_status='PENDING_REVIEW',records=records))
 all_records=[]
 for b in CAT:
  old=R/f'public/assets/dogs/full/{b["slug"]}-full.png'
  item=dict(**b,original=dict(path=rel(old),style='DPL-ILL-1.2',sha256=sha(old)),doodle=dict(path=f'public/assets/dogs/doodle-v01/{b["id"]}-full.png',production_status='PLANNED',technical_pass=None,human_review_status='PENDING_REVIEW'))
  baseline=next((r for r in BASE if r['id']==b['id']),None);new=next((r for r in records if r['id']==b['id']),None)
  if baseline:
   dst=OUT/f'{b["id"]}-full.png';assert sha(dst)==baseline['sha256'];q=metrics(Image.open(dst))
   item['doodle'].update(production_status='GENERATED',technical_pass=q['technical_pass'],human_review_status='APPROVED',approval='Explicit user approval 2026-11-02 Asia/Shanghai of six Doodle V01 tests and series language',sha256=sha(dst),source_test=f'public/assets/dogs/style-tests/doodle-v01/{baseline["path"]}',source_record=f'public/assets/dogs/style-tests/doodle-v01/{b["id"]}/qc.json')
  elif new:item['doodle'].update(production_status='GENERATED',technical_pass=True,human_review_status='PENDING_REVIEW',sha256=new['sha256'],record=f'docs/asset-production/doodle/batch01/{b["id"]}/record.json')
  all_records.append(item)
 write(DOC/'manifest.json',dict(style='DPL-DOODLE-1.0',counts=dict(total=120,generated=18,technical_pass=18,human_approved=6,pending_review_generated=12,planned=102),records=all_records))
 pending=[b['id'] for b in CAT if b['id'] not in {r['id'] for r in BASE}]
 batches=[pending[i:i+12] for i in range(0,len(pending),12)]
 assert list(map(len,batches))==[12]*9+[6]
 write(DOC/'schedule.json',dict(batches=[dict(batch=i+1,ids=v,status='GENERATED_PENDING_REVIEW' if i==0 else 'NOT_AUTHORIZED_UNTIL_PRIOR_REVIEW') for i,v in enumerate(batches)]))
 print('Finalized 12 outputs and 120-entry version manifest; six approved baselines unchanged.')
if __name__=='__main__':
 if sys.argv[1]=='ingest':ingest(sys.argv[2],sys.argv[3],sys.argv[4] if len(sys.argv)>4 else 'v01')
 elif sys.argv[1]=='finalize':finalize()
 else:raise SystemExit('ingest ID PATH | finalize')
