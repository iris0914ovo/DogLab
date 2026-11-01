# round3-b03-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存12张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号219项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B037|挪威猎麋犬|[PNG](../../public/assets/dogs/full/norwegian-elkhound-full.png)|[JSON](records/B037-full-v01.json)|PASS|
|B038|挪威伦德猎犬|[PNG](../../public/assets/dogs/full/norwegian-lundehund-full.png)|[JSON](records/B038-full-v01.json)|PASS|
|B039|挪威布哈德犬|[PNG](../../public/assets/dogs/full/norwegian-buhund-full.png)|[JSON](records/B039-full-v01.json)|PASS|
|B040|冰岛牧羊犬|[PNG](../../public/assets/dogs/full/icelandic-sheepdog-full.png)|[JSON](records/B040-full-v01.json)|PASS|
|B041|瑞典瓦尔杭犬|[PNG](../../public/assets/dogs/full/swedish-vallhund-full.png)|[JSON](records/B041-full-v01.json)|PASS|
|B042|荷兰毛狮犬|[PNG](../../public/assets/dogs/full/keeshond-full.png)|[JSON](records/B042-full-v01.json)|PASS|
|B043|博美犬|[PNG](../../public/assets/dogs/full/pomeranian-full.png)|[JSON](records/B043-full-v01.json)|PASS|
|B044|德国狐狸犬（中型）|[PNG](../../public/assets/dogs/full/german-spitz-mittel-full.png)|[JSON](records/B044-full-v01.json)|PASS|
|B045|日本狐狸犬|[PNG](../../public/assets/dogs/full/japanese-spitz-full.png)|[JSON](records/B045-full-v01.json)|PASS|
|B046|欧亚犬|[PNG](../../public/assets/dogs/full/eurasier-full.png)|[JSON](records/B046-full-v01.json)|PASS|
|B047|北海道犬|[PNG](../../public/assets/dogs/full/hokkaido-full.png)|[JSON](records/B047-full-v01.json)|PASS|
|B048|四国犬|[PNG](../../public/assets/dogs/full/shikoku-full.png)|[JSON](records/B048-full-v01.json)|PASS|

[合版 round3-b03-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b03-dpl-ill-1.2-v01-paper.png)

[合版 round3-b03-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b03-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: compact grey Elkhound, short-legged Vallhund, abundant Keeshond/Pomeranian coats and leaner Hokkaido/Shikoku remain visible. White spitz B034/B044/B045 have naturally similar appearance and are flagged for final human comparison rather than declared fully distinct; Lundehund toe anatomy requires close human review. No obvious ear/tail/paw clipping; no human approval assigned.
