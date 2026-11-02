"""Reproduce technical fitting/QC and review sheets from retained raw outputs.
Run from any directory with Pillow and numpy installed. Never regenerates images.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
import json,hashlib
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'generation.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
for row in rows:
 p=ROOT/row['id'];raw=p/'raw.png';prompt=p/'prompt.txt'
 with Image.open(raw) as original:
  assert original.format=='PNG' and original.mode=='RGBA'
  source=original.copy()
 # Fit complete subject uniformly on a transparent square. Preserve raw source.
 # Near-zero residues removed and near-opaque interiors normalized like V1 pipeline.
 a=np.array(source.getchannel('A'));a[a<=2]=0
 source.putalpha(Image.fromarray(a));bbox=source.getchannel('A').getbbox();assert bbox
 crop=source.crop(bbox);scale=816/max(crop.size);size=tuple(round(x*scale) for x in crop.size)
 crop=crop.resize(size,Image.Resampling.LANCZOS)
 a=np.array(crop.getchannel('A'));a[a<=2]=0
 core=np.array(Image.fromarray((a>128).astype('uint8')*255).filter(ImageFilter.MinFilter(9)))==255
 a[core]=255;a[a>=250]=255
 crop.putalpha(Image.fromarray(a))
 canvas=Image.new('RGBA',(1024,1024),(0,0,0,0));pos=((1024-size[0])//2,(1024-size[1])//2)
 canvas.paste(crop,pos)
 out=ROOT/f"{row['slug']}-full.png"
 canvas.save(out)
 with Image.open(out) as check:
  assert check.format=='PNG';check.load();a=np.array(check.getchannel('A'));bb=check.getchannel('A').getbbox()
  core=np.array(check.getchannel('A').point(lambda v:255 if v>128 else 0).filter(ImageFilter.MinFilter(9)))==255
  margins=[bb[0],bb[1],1024-bb[2],1024-bb[3]]
  qc=dict(size=list(check.size),mode=check.mode,alpha_min=int(a.min()),alpha_max=int(a.max()),transparent_pixels=int((a==0).sum()),opaque_pixels=int((a==255).sum()),partial_alpha_pixels=int(((a>0)&(a<255)).sum()),translucent_core_pixels=int(((a<255)&core).sum()),bbox=list(bb),margins=margins)
 qc['checks']=dict(png=True,size=qc['size']==[1024,1024],rgba=qc['mode']=='RGBA',transparent_background=qc['alpha_min']==0 and qc['opaque_pixels']>0,opaque_core=qc['translucent_core_pixels']==0,antialias=qc['partial_alpha_pixels']>0,safe_margin=min(margins)>=100)
 qc['technical_pass']=all(qc['checks'].values())
 rec={**row,'production_status':'STYLE_TEST','human_review_status':'PENDING_REVIEW','tool':'image_gen__imagegen','model_id':None,'raw_path':str(raw.relative_to(ROOT)),'raw_sha256':sha(raw),'raw_size':list(source.size),'prompt_path':str(prompt.relative_to(ROOT)),'prompt_sha256':sha(prompt),'path':out.name,'sha256':sha(out),'pixels_sha256':hashlib.sha256(canvas.tobytes()).hexdigest(),'processing':{'crop':list(bbox),'uniform_scale':scale,'size':list(size),'position':list(pos),'alpha':'remove <=2 residues; eroded core and >=250 to255; remaining edge alpha preserved; originals retained'},'qc':qc}
 (p/'qc.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n');records.append(rec)
font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',22)
small=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',18)
for theme,bg,fg in [('paper','#F5F0E6','#20201D'),('ink','#20201D','#F5F0E6')]:
 sheet=Image.new('RGB',(1536,1152),bg);draw=ImageDraw.Draw(sheet)
 for i,r in enumerate(records):
  x=(i%3)*512;y=(i//3)*576
  im=Image.open(ROOT/r['path']).resize((480,480),Image.Resampling.LANCZOS)
  sheet.paste(im,(x+16,y+4),im)
  draw.text((x+20,y+488),r['id']+' '+r['name'],font=font,fill=fg)
  draw.text((x+20,y+530),'DOODLE V01 / STYLE_TEST / 待审核',font=small,fill=fg)
 sheet.save(ROOT/f'contact-{theme}.png')
# Literal six-across view supplements the larger two-row technical review.
sheet=Image.new('RGB',(1800,360),'#F5F0E6');draw=ImageDraw.Draw(sheet)
for i,r in enumerate(records):
 im=Image.open(ROOT/r['path']).resize((300,300),Image.Resampling.LANCZOS);sheet.paste(im,(i*300,0),im)
 draw.text((i*300+18,310),r['id']+' '+r['name'],font=small,fill='#20201D')
sheet.save(ROOT/'contact-lineup.png')
assert len(records)==6 and len({r['sha256'] for r in records})==6 and len({r['pixels_sha256'] for r in records})==6
assert all(r['qc']['technical_pass'] for r in records)
manifest={'batch':'Naive Dog Doodle V01','production_status':'STYLE_TEST','human_review_status':'PENDING_REVIEW','scope':'Six full-body breed tests only; stop for user review','records':records,'previews':['contact-paper.png','contact-ink.png','contact-lineup.png']}
(ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(ROOT/'SHA256SUMS').write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='SHA256SUMS'))
print('PASS: six independent 1024 PNG RGBA outputs, transparency, opaque core, safe margins, unique binary/pixels.')
