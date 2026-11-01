# 第二轮12种犬种批次质检与交付报告

## 执行范围与风格

批次 `round2-dpl-ill-1.2-v01`，12次独立 image_gen__imagegen 调用，使用用户已认可的第一轮六图合版作画风参考，未复制同一身体模板。未调用独立API、未要求用户手工生成或上传、未生成第三轮102种。每次请求透明背景，实际返回本地真实PNG路径；直接复制二进制，不在消息中输出整张Base64。未发生失败或重试，每张实际尝试1次。

当前风格 DPL-ILL-1.2：手绘绘本质感、深棕自然外轮廓、层次毛发笔触与色块、柔和阴影和轻微纸感，色彩温暖且服从自然毛色。旧规范完整归档在 docs/history/ILLUSTRATION_GUIDE_V1.1.md；用户认可及新风格已写入 ILLUSTRATION_REVIEW。第一轮六图仅标整体风格基准获认可，不自动批准第二轮新图或未制作肖像。

## 技术质检结果

12/12通过基础技术检查：PNG、1024×1024、RGBA、alpha背景为0、主体核心为255、自然边缘抗锯齿、最长边约819px、安全边至少102px。采用同一个缩放因子等比适配，不拉伸躯干。保存原始高清图、Prompt全文与哈希、输出文件与SHA256、工具/风格版本和处理记录；工具没有暴露具体模型ID和请求ID，记为null。

原始图可能有近不透明alpha=253等情况：沿用已验证处理器，清理alpha<=2残留、将腐蚀主体核心及近不透明像素规范化为255，保留边缘抗锯齿。原图不改写，不把白色背景改RGBA冒充真实透明，也不硬阈值切除细毛。原始轮廓靠近画布边缘时在raw_qc与source_alpha_touches_canvas记录，正式安全边不保证原始解剖绝无缺损，因此另作AI视觉检视并保留人工审核。

跨首轮与本轮全部18张的文件及像素SHA256均唯一。8×8轮廓近似哈希出现34对相似信号（包括跨批比较），这是一种低分辨率姿态相似警告，不是34张重复图；AI逐犬检查合版可见不同骨架与毛质，原始信号在批次JSON中保留，不据此掩盖或删除实际图片。简单图像统计不能保证犬种识别，耳口鼻、尾型和骨架仍以视觉审核为准。

## 逐犬文件与AI视觉检查

| Breed ID | 犬种 | 实际PNG | 记录 | 基础技术QC | AI视觉观察（不等于人工批准） |
|---|---|---|---|---|---|
| B012 | 腊肠犬 | [PNG](../../public/assets/dogs/full/dachshund-full.png) | [JSON](records/B012-full-v01.json) | PASS | 长身短腿、柔软长垂耳、长口吻和细长尾可辨；保留自然脊背，未见明显裁切。 |
| B015 | 迷你雪纳瑞 | [PNG](../../public/assets/dogs/full/miniature-schnauzer-full.png) | [JSON](records/B015-full-v01.json) | PASS | 椒盐刚毛、胡须眉毛、自然折耳与近方形躯干可辨；尾部自然完整。 |
| B023 | 纽芬兰犬 | [PNG](../../public/assets/dogs/full/newfoundland-full.png) | [JSON](records/B023-full-v01.json) | PASS | 宽头深胸、大脚掌、粗壮四肢与厚实深色双层毛可辨；深底细节需用户复核。 |
| B025 | 灵缇 | [PNG](../../public/assets/dogs/full/greyhound-full.png) | [JSON](records/B025-full-v01.json) | PASS | 窄长头、玫瑰折耳、深胸收腰和修长四肢清楚，与厚实犬种轮廓不同。 |
| B029 | 蝴蝶犬 | [PNG](../../public/assets/dogs/full/papillon-full.png) | [JSON](records/B029-full-v01.json) | PASS | 蝶翼耳、耳缘丝质饰毛、轻巧骨架和流苏尾可辨；细耳毛没有被硬切。 |
| B033 | 阿拉斯加雪橇犬 | [PNG](../../public/assets/dogs/full/alaskan-malamute-full.png) | [JSON](records/B033-full-v01.json) | PASS | 头胸比哈士奇更宽厚、脚掌骨量更大；同色系仍有雪橇犬外观相似，差异充分性留给用户集中审核。 |
| B054 | 秘鲁无毛犬 | [PNG](../../public/assets/dogs/full/peruvian-hairless-dog-full.png) | [JSON](records/B054-full-v01.json) | PASS | 可见裸露皮肤色面、颈胸自然褶皱、大立耳和细长裸尾，不是短毛犬简单去色。 |
| B070 | 科蒙多犬 | [PNG](../../public/assets/dogs/full/komondor-full.png) | [JSON](records/B070-full-v01.json) | PASS | 白色自然独立绳状毛束遍及身体与尾，非普通长毛；足掌可见，毛下结构需人工最终复核。 |
| B078 | 英国可卡犬 | [PNG](../../public/assets/dogs/full/english-cocker-spaniel-full.png) | [JSON](records/B078-full-v01.json) | PASS | 低位长垂耳、丝质饰毛、自然长尾及独立头部比例可辨。 |
| B104 | 法国斗牛犬 | [PNG](../../public/assets/dogs/full/french-bulldog-full.png) | [JSON](records/B104-full-v01.json) | PASS | 保留自然短口吻、可辨鼻部、蝙蝠耳与正常四肢支撑，未见极端压平或痛苦喘气；插画观察不能诊断实际呼吸道健康。 |
| B116 | 苏格兰梗 | [PNG](../../public/assets/dogs/full/scottish-terrier-full.png) | [JSON](records/B116-full-v01.json) | PASS | 小立耳、长头胡须、低身短腿与黑色刚毛可辨，区别于雪纳瑞折耳。 |
| B120 | 巴吉度猎犬 | [PNG](../../public/assets/dogs/full/basset-hound-full.png) | [JSON](records/B120-full-v01.json) | PASS | 极长低垂耳、低矮厚实躯干、短粗腿、大掌与三色短毛可辨，非细腿腊肠模板。 |

## 4×3整批合版

- [paper 底色合版](../../public/assets/dogs/review/round2-dpl-ill-1.2-v01-paper.png)
- [ink 底色合版](../../public/assets/dogs/review/round2-dpl-ill-1.2-v01-ink.png)
- [mist 底色合版](../../public/assets/dogs/review/round2-dpl-ill-1.2-v01-mist.png)

科蒙多犬呈现独立白色绳束；秘鲁犬呈现裸露皮肤而非短毛去色；阿拉斯加有更宽厚的头胸与骨量，但与哈士奇属于同类外观，差异充分性仍待用户确认。法国斗牛犬保持自然短口吻和鼻部结构，未画夸张压扁或痛苦喘气；插画检查不是临床健康判断。深色纽芬兰与苏格兰梗在ink底对比度较低，应结合paper/mist合版一起审查。

本轮没有基础技术失败文件，也没有人工批准的第二轮图片。12张均为GENERATED且待集中审核，不伪造APPROVED。32种正式人格的肖像仍未生产；资产清单按所需最低进度汇总，正式人格只有全身图时总体仍为PLANNED，实际文件栏和逐文件记录明确已生成，避免重复生产。

## 同步与停止点

本轮将独立PNG、原始图、Prompt、记录、三底4×3合版、清单和本报告推送到 work，随后从独立临时Git对象库读取远程提交与每个图片blob核对SHA256并实际解码。验证证据见 verification 目录；在验证前不声称已完成上传。不得修改main、不得强制推送、不得覆盖第一轮已存在PNG。

交付后暂停，等待用户一次性审核这12种，不自动开始第三轮102种、肖像或网站开发。
