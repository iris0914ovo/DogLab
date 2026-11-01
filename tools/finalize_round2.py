"""Finalize and validate round2 actual artifacts. No generation or API calls."""
from pathlib import Path
import json,re,hashlib,itertools,shutil
import numpy as np
from PIL import Image,ImageFilter
from illustration_batch import sha
from illustration_round2 import pipeline
ROOT=Path(__file__).resolve().parents[1];IDS=pipeline.IDS;BATCH=pipeline.BATCH
NOTES={
'B012':'长身短腿、柔软长垂耳、长口吻和细长尾可辨；保留自然脊背，未见明显裁切。',
'B015':'椒盐刚毛、胡须眉毛、自然折耳与近方形躯干可辨；尾部自然完整。',
'B023':'宽头深胸、大脚掌、粗壮四肢与厚实深色双层毛可辨；深底细节需用户复核。',
'B025':'窄长头、玫瑰折耳、深胸收腰和修长四肢清楚，与厚实犬种轮廓不同。',
'B029':'蝶翼耳、耳缘丝质饰毛、轻巧骨架和流苏尾可辨；细耳毛没有被硬切。',
'B033':'头胸比哈士奇更宽厚、脚掌骨量更大；同色系仍有雪橇犬外观相似，差异充分性留给用户集中审核。',
'B054':'可见裸露皮肤色面、颈胸自然褶皱、大立耳和细长裸尾，不是短毛犬简单去色。',
'B070':'白色自然独立绳状毛束遍及身体与尾，非普通长毛；足掌可见，毛下结构需人工最终复核。',
'B078':'低位长垂耳、丝质饰毛、自然长尾及独立头部比例可辨。',
'B104':'保留自然短口吻、可辨鼻部、蝙蝠耳与正常四肢支撑，未见极端压平或痛苦喘气；插画观察不能诊断实际呼吸道健康。',
'B116':'小立耳、长头胡须、低身短腿与黑色刚毛可辨，区别于雪纳瑞折耳。',
'B120':'极长低垂耳、低矮厚实躯干、短粗腿、大掌与三色短毛可辨，非细腿腊肠模板。'}
def finalize():
 records=[]
 ref='public/assets/dogs/review/round1-dpl-ill-1.1-v02-paper.png'
 for id in IDS:
  path=ROOT/f'docs/asset-production/records/{id}-full-v01.json';r=json.loads(path.read_text())
  assert r['style_version']=='DPL-ILL-1.2' and r['breed_id']==id
  assert sha(ROOT/r['path'])==r['sha256'] and sha(ROOT/r['raw_path'])==r['raw_sha256'] and sha(ROOT/r['prompt_path'])==r['prompt_sha256']
  im=Image.open(ROOT/r['path']);im.load();a=np.array(im.getchannel('A'));bbox=im.getchannel('A').getbbox()
  assert im.mode=='RGBA' and im.size==(1024,1024) and im.format=='PNG'
  assert a.min()==0 and a.max()==255 and ((a>0)&(a<255)).any()
  assert min(bbox[0],bbox[1],1024-bbox[2],1024-bbox[3])>=102
  core=np.array(im.getchannel('A').point(lambda x:255 if x>128 else 0).filter(ImageFilter.MinFilter(9)))==255
  assert (a[core]==255).all()
  r['reference_images']=[{'path':ref,'sha256':sha(ROOT/ref),'scope':'User-approved round1 overall style only; no body templates'}]
  r['tool_parameters']={'transparent_background':True,'referenced_image_paths':[str(ROOT/ref)]}
  r['qc']['visual_status']='NEEDS_USER_REVIEW';r['qc']['visual_notes']=NOTES[id]
  r['qc']['source_alpha_touches_canvas']=any([r['raw_qc']['bbox'][0]==0,r['raw_qc']['bbox'][1]==0,r['raw_qc']['bbox'][2]==r['raw_qc']['size'][0],r['raw_qc']['bbox'][3]==r['raw_qc']['size'][1]])
  rgb=np.array(im)[:,:,:3];mask=a>128
  r['qc']['dark_pixel_fraction']=float(((rgb.mean(axis=2)<70)&mask).sum()/mask.sum())
  r['qc']['color_validation']='AI inspection: warm natural coat/skin colors; numeric pixel palette is not a breed classifier'
  r['qc']['integrity_validation']='AI inspected full 4x3 contact sheet: no obvious missing ear/tail/paws; anatomy still needs human review'
  path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');records.append(r)
 all_records=[json.loads(f.read_text()) for f in (ROOT/'docs/asset-production/records').glob('B*-full-*.json')]
 assert len(all_records)==18 and len({r['sha256'] for r in all_records})==18 and len({r['pixels_sha256'] for r in all_records})==18
 hashes={}
 for r in all_records:
  a=np.array(Image.open(ROOT/r['path']).getchannel('A').resize((8,8),Image.Resampling.BOX));hashes[r['breed_id']]=a>a.mean()
 near=[]
 for (a,ha),(b,hb) in itertools.combinations(hashes.items(),2):
  distance=int((ha!=hb).sum())
  if distance<8 and (a in IDS or b in IDS):near.append(dict(ids=[a,b],silhouette_hamming=distance,note='Near-silhouette signal only; AI contact-sheet review found distinct breed morphology, pending human review'))
 contacts=[f'public/assets/dogs/review/{BATCH}-{label}.png' for label in ['paper','ink','mist']]
 for path in contacts:
  im=Image.open(ROOT/path);im.load();assert im.size==(2048,1740)
 batch=dict(batch_id=BATCH,style_version='DPL-ILL-1.2',breed_ids=IDS,record_paths=[f"docs/asset-production/records/{id}-full-v01.json" for id in IDS],contact_sheets=contacts,grid=[4,3],technical_pass_count=12,failed_ids=[],generation_attempts_per_image=1,exact_duplicate_count=0,near_silhouette_warnings=near,human_review_status='PLANNED',scope='12 full bodies only; no portraits; stop before round3 102',reference_style_user_approved=True)
 out=ROOT/f'docs/asset-production/batches/{BATCH}.json';out.write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n')
 p=ROOT/'docs/ASSET_MANIFEST.md';s=p.read_text();first=s.index('来源：');last=s.index('## 状态约定')
 s=s[:first]+'''来源：BREED_DATA.md 的120条记录，名称、英文、slug与正式人格标记不变。当前共18张全身PNG实际落库：首轮6张用户认可整体画风，第二轮12张GENERATED且待集中审核；32张肖像未制作。表中目标路径与实际文件分列，不以计划路径冒充成品。所有肖像未制作的正式人格仍按所需资产最低进度聚合为PLANNED；普通图鉴只有全身需求，生成后制作状态为GENERATED。第一轮画风认可不扩展成第二轮批准。\n\n'''+s[last:]
 # Replace stale summary, retaining operational status rules.
 start=s.index('生产阶段新增逐文件证据记录：');end=s.index('## 120 条索引')
 s=s[:start]+'''逐文件证据见 docs/asset-production/records/，包含Prompt、风格版本、工具、实际文件与SHA256、处理参数、基础QC及视觉意见。首轮真实六图已获用户整体画风认可，新一轮仍待人工审核。旧对话样图未上传不影响当前真实产物记录；品牌Logo不在此次犬图认可范围。\n\n'''+s[end:]
 lines=[]
 for line in s.splitlines():
  if re.match(r'^\| B\d{3} \|',line):
   row=line.strip('| ').split(' | ');id=row[0]
   if id in IDS:
    row[7]='PLANNED' if row[4]=='是' else 'GENERATED';row[8]='PLANNED'
    r=next(r for r in records if r['breed_id']==id)
    row[9]='全身 GENERATED：'+r['path']+('；肖像未制作' if row[4]=='是' else '')
    row[10]='第二轮AI检查：'+NOTES[id]+' 待用户审核。'
   elif id in ['B001','B002','B003','B004','B005','B007']:
    row[9]=row[9].replace('全身 GENERATED：','全身 REVIEWED（用户认可画风）：')
    row[10]+=' 第一轮整体画风已获用户认可，作为DPL-ILL-1.2基准；不代表肖像批准。'
   line='| '+' | '.join(row)+' |'
  lines.append(line)
 s='\n'.join(lines)+'\n';start=s.index('\n本轮 6 张新全身候选')
 s=s[:start]+f'\n共18张实际全身PNG：首轮6张为认可的画风基准；第二轮12张为GENERATED并待集中审核。第二轮4×3浅/深/雾蓝底合版与质检见 [批次记录](asset-production/batches/{BATCH}.json)。未生成第三轮102种或任何肖像，0张第二轮人工批准。\n';p.write_text(s)
 # Actual production update; preserve guide history section verbatim.
 p=ROOT/'docs/ILLUSTRATION_GUIDE.md';s=p.read_text().replace('## 17｜分轮生产计划与执行进度','## 17｜分轮生产计划与执行进度\n\n当前：第一轮6图已获用户认可整体风格；第二轮12图实际生成、归档并基础QC通过，等待集中审核；第三轮102种未启动，肖像未制作。')
 s=s.replace('本次只是生产排程，不代表已启动任何一轮生产。','原排程现已推进至第二轮实际生产，具体文件和结果见第二轮批次记录。')
 p.write_text(s)
 print('PASS 12 outputs, 3 actual 4x3 sheets, 18 globally unique images; near silhouette signals:',len(near))
 return batch
if __name__=='__main__':finalize()
