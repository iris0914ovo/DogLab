"""Local ingestion/QC for real image_gen outputs; never calls paid APIs.
Usage: python3 tools/illustration_batch.py ingest B001 /absolute/tool/output.png
       python3 tools/illustration_batch.py finalize
"""
from pathlib import Path
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import numpy as np
import hashlib,json,sys,shutil,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
IDS=['B001','B002','B003','B004','B005','B007']
BATCH='round1-dpl-ill-1.1-v02'
VERSION='v02'
STYLE='DPL-ILL-1.1'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write_new(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
def catalog():
 out={}
 for line in (ROOT/'docs/BREED_DATA.md').read_text().splitlines():
  row=line.strip('| ').split(' | ')
  if re.match(r'^\| B\d{3} \|',line) and len(row)==8:out[row[0]]=row
 assert len(out)==120
 return out
def metrics(im):
 a=np.array(im.getchannel('A'));bbox=im.getchannel('A').getbbox()
 core=np.array(im.getchannel('A').point(lambda x:255 if x>128 else 0).filter(ImageFilter.MinFilter(9)))==255
 return dict(size=list(im.size),mode=im.mode,alpha_min=int(a.min()),alpha_max=int(a.max()),transparent_pixels=int((a==0).sum()),opaque_pixels=int((a==255).sum()),partial_alpha_pixels=int(((a>0)&(a<255)).sum()),bbox=list(bbox) if bbox else None,core_translucent_pixels=int(((a<255)&core).sum()),core_pixels=int(core.sum()))
def ingest(id,source):
 assert id in IDS
 row=catalog()[id];slug=row[3]
 base=ROOT/f'artifacts/illustrations/{id}/full/{VERSION}';base.mkdir(parents=True,exist_ok=True)
 raw=base/'raw.png';source=Path(source).resolve()
 if raw.exists():assert sha(raw)==sha(source),'Raw exists with different content'
 else:shutil.copyfile(source,raw)
 dst=ROOT/f'public/assets/dogs/full/{slug}-full.png'
 record=ROOT/f'docs/asset-production/records/{id}-full-{VERSION}.json'
 if record.exists():
  r=json.loads(record.read_text());assert dst.exists() and sha(dst)==r['sha256'];print(id,'already recorded; skipped');return
 assert not dst.exists(),'Never overwrite existing final file'
 with Image.open(raw) as opened:
  assert opened.format=='PNG' and opened.mode=='RGBA','Native PNG RGBA required'
  opened.load();im=opened.copy()
 raw_qc=metrics(im);assert raw_qc['transparent_pixels']>0 and raw_qc['opaque_pixels']>0
 # Technical mask normalization only. Keep original source and all natural edge alpha.
 a=np.array(im.getchannel('A'));a[a<=2]=0
 core=np.array(Image.fromarray((a>128).astype('uint8')*255).filter(ImageFilter.MinFilter(9)))==255
 core_adjusted=int(((a<255)&core).sum());near_opaque=int(((a>=250)&(a<255)).sum())
 a[core]=255;a[a>=250]=255
 im.putalpha(Image.fromarray(a))
 box=im.getchannel('A').getbbox();assert box
 cropped=im.crop(box);scale=819/max(cropped.size)
 # Uniform scale; integer raster rounding affects each dimension by at most one pixel.
 size=tuple(max(1,round(x*scale)) for x in cropped.size)
 cropped=cropped.resize(size,Image.Resampling.LANCZOS)
 # Resize can introduce internal alpha rounding; interior mask is opaque, AA edges retained.
 a=np.array(cropped.getchannel('A'));core=np.array(Image.fromarray((a>128).astype('uint8')*255).filter(ImageFilter.MinFilter(9)))==255
 a[core]=255;a[a>=250]=255;cropped.putalpha(Image.fromarray(a))
 canvas=Image.new('RGBA',(1024,1024),(0,0,0,0));x=(1024-size[0])//2
 y=(1024-size[1])//2 if id=='B003' else 921-size[1]
 canvas.paste(cropped,(x,y)) # paste WITHOUT mask: avoids squaring alpha
 dst.parent.mkdir(parents=True,exist_ok=True)
 with dst.open('xb') as f:canvas.save(f,format='PNG')
 with Image.open(dst) as check:check.load();qc=metrics(check)
 bbox=qc['bbox'];margins=[bbox[0],bbox[1],1024-bbox[2],1024-bbox[3]]
 checks=dict(decodes=True,png=True,size=qc['size']==[1024,1024],rgba=qc['mode']=='RGBA',real_transparency=qc['transparent_pixels']>0 and qc['opaque_pixels']>0,safe_margin=min(margins)>=102,subject_size=abs(max(bbox[2]-bbox[0],bbox[3]-bbox[1])-819)<=2,opaque_core=qc['core_translucent_pixels']==0,antialias_present=qc['partial_alpha_pixels']>0)
 qc.update(checks=checks,technical_pass=all(checks.values()),margins=margins)
 prompt=base/'prompt.txt'
 r=dict(breed_id=id,name=row[1],slug=slug,asset_kind='full',batch_id=BATCH,style_version=STYLE,prompt_version=f'{id}-full-{VERSION}',prompt_path=str(prompt.relative_to(ROOT)),prompt_sha256=sha(prompt),tool='image_gen__imagegen',model=None,request_id=None,tool_source_path=str(source),saved_at=datetime.now(timezone.utc).isoformat(),raw_path=str(raw.relative_to(ROOT)),raw_sha256=sha(raw),raw_qc=raw_qc,path=str(dst.relative_to(ROOT)),sha256=sha(dst),pixels_sha256=hashlib.sha256(canvas.tobytes()).hexdigest(),processing=dict(raw_dimensions=list(im.size),crop_bbox=box,uniform_scale=scale,resized_dimensions=size,position=[x,y],alpha_normalization='remove alpha<=2 residue; set eroded interior and near-opaque alpha>=250 to255; preserve edge antialias',core_adjusted=core_adjusted,near_opaque_adjusted=near_opaque),qc=qc,production_status='GENERATED',human_review_status='PLANNED',visual_review='AI inspection only; breed morphology/style/texture require user batch review; no approval',generation_attempts=1)
 write_new(record,r)
 print(json.dumps(dict(id=id,path=r['path'],sha256=r['sha256'],qc=qc),ensure_ascii=False))
def finalize():
 records=[json.loads((ROOT/f'docs/asset-production/records/{id}-full-{VERSION}.json').read_text()) for id in IDS]
 existing_batch=ROOT/f'docs/asset-production/batches/{BATCH}.json'
 if existing_batch.exists():
  for r in records: assert sha(ROOT/r['path'])==r['sha256'], 'Existing output changed'
  b=json.loads(existing_batch.read_text())
  for path in b['contact_sheets']: assert (ROOT/path).is_file(), 'Existing preview missing'
  print('Existing batch preserved; no regeneration or overwrite');return
 assert len({r['sha256'] for r in records})==6,'Duplicate binary'
 assert len({r['pixels_sha256'] for r in records})==6,'Duplicate pixels'
 font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
 font=ImageFont.truetype(font_path,24);small=ImageFont.truetype(font_path,18)
 review=ROOT/'public/assets/dogs/review';review.mkdir(parents=True,exist_ok=True)
 names=[]
 for label,bg in [('paper','#F5F0E6'),('ink','#20201D'),('mist','#C7D8DB')]:
  sheet=Image.new('RGB',(1536,1160),bg);draw=ImageDraw.Draw(sheet);color='#F5F0E6' if label=='ink' else '#20201D'
  for i,r in enumerate(records):
   x=(i%3)*512;y=(i//3)*580
   im=Image.open(ROOT/r['path']).convert('RGBA').resize((480,480),Image.Resampling.LANCZOS)
   sheet.paste(im,(x+16,y+8),im)
   draw.text((x+22,y+492),f"{r['breed_id']} {r['name']}",font=font,fill=color)
   draw.text((x+22,y+532),'v02 | '+('QC PASS' if r['qc']['technical_pass'] else 'QC FAIL')+' | 待人工审核',font=small,fill=color)
  path=review/f'{BATCH}-{label}.png'
  assert not path.exists()
  sheet.save(path);names.append(str(path.relative_to(ROOT)))
 batch=dict(batch_id=BATCH,records=[f"docs/asset-production/records/{r['breed_id']}-full-v02.json" for r in records],contact_sheets=names,technical_pass_count=sum(r['qc']['technical_pass'] for r in records),exact_duplicates=False,human_review_status='PLANNED',scope='6 full-body candidates only; no portraits; stop before round2')
 write_new(ROOT/f'docs/asset-production/batches/{BATCH}.json',batch)
 # Preserve original review notes, names and aggregate status (portraits still PLANNED).
 p=ROOT/'docs/ASSET_MANIFEST.md';s=p.read_text();lines=[]
 for line in s.splitlines():
  if re.match(r'^\| B\d{3} \|',line):
   row=line.strip('| ').split(' | ');r=next((r for r in records if r['breed_id']==row[0]),None)
   if r:row[9]=f"全身 GENERATED：{r['path']}；肖像未制作";line='| '+' | '.join(row)+' |'
  lines.append(line)
 s='\n'.join(lines)+'\n'
 s=s.replace('这些样图尚未上传本仓库；两种状态均为 PLANNED。','旧样图未上传；本轮另由图像工具新生成 6 张全身候选并保存到仓库。32 种正式犬格的肖像仍未制作，按最低进度汇总的状态仍为 PLANNED；逐全身图状态 GENERATED，人工待审核。')
 s=s.replace('当前不存在，不是实际文件路径或已完成链接；“实际文件”栏如实记录未上传。','未制作条目并不存在；实际已生成的六张全身图仅以“实际文件”栏与逐图记录为证。')
 s=s.replace('目前项目内无图像文件；六只在 ChatGPT 对话中已有审核样图，但未取得源文件、哈希及逐文件版本，不能把外部审核等同于已上传或人工批准，不捏造这些记录。','旧对话样图仍无源文件；本轮六张新全身候选有实际文件、Prompt 与 SHA256，逐图记录位于 docs/asset-production/records/。新图尚未人工批准，不能把历史审核直接迁移到新版本。')
 s=s.replace('目录内仅有 `.gitkeep` 用于 Git 保留空目录，不是占位图片。当前 0 张狗狗图像落库、0 张人工批准；外部对话样图共 6 张，其审核意见由用户转述，见 [ILLUSTRATION_REVIEW.md](ILLUSTRATION_REVIEW.md)。不能把未上传记成未曾在外部生成，也不能把方向通过记成正式资产批准。','本轮 6 张新全身候选已落库（GENERATED），另有三底六犬合版，0 张人工批准；旧对话样图仍未上传。历史审核意见见 [ILLUSTRATION_REVIEW.md](ILLUSTRATION_REVIEW.md)，本轮数据见 [批次记录](asset-production/batches/'+BATCH+'.json)。未生成其余 114 种或任何肖像。')
 p.write_text(s)
 print(json.dumps(batch,ensure_ascii=False))
if __name__=='__main__':
 if sys.argv[1]=='ingest':ingest(sys.argv[2],sys.argv[3])
 elif sys.argv[1]=='finalize':finalize()
 else:raise SystemExit('Unknown command')
