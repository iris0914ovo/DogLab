# round3-b02-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存12张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号144项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B021|大丹犬|[PNG](../../public/assets/dogs/full/great-dane-full.png)|[JSON](records/B021-full-v01.json)|PASS|
|B022|伯恩山犬|[PNG](../../public/assets/dogs/full/bernese-mountain-dog-full.png)|[JSON](records/B022-full-v01.json)|PASS|
|B024|圣伯纳犬|[PNG](../../public/assets/dogs/full/saint-bernard-full.png)|[JSON](records/B024-full-v01.json)|PASS|
|B026|惠比特犬|[PNG](../../public/assets/dogs/full/whippet-full.png)|[JSON](records/B026-full-v01.json)|PASS|
|B027|巴仙吉犬|[PNG](../../public/assets/dogs/full/basenji-full.png)|[JSON](records/B027-full-v01.json)|PASS|
|B028|大麦町犬|[PNG](../../public/assets/dogs/full/dalmatian-full.png)|[JSON](records/B028-full-v01.json)|PASS|
|B030|骑士查理王小猎犬|[PNG](../../public/assets/dogs/full/cavalier-king-charles-spaniel-full.png)|[JSON](records/B030-full-v01.json)|PASS|
|B031|比熊犬|[PNG](../../public/assets/dogs/full/bichon-frise-full.png)|[JSON](records/B031-full-v01.json)|PASS|
|B032|松狮犬|[PNG](../../public/assets/dogs/full/chow-chow-full.png)|[JSON](records/B032-full-v01.json)|PASS|
|B034|美国爱斯基摩犬|[PNG](../../public/assets/dogs/full/american-eskimo-dog-full.png)|[JSON](records/B034-full-v01.json)|PASS|
|B035|芬兰拉普猎犬|[PNG](../../public/assets/dogs/full/finnish-lapphund-full.png)|[JSON](records/B035-full-v01.json)|PASS|
|B036|芬兰狐狸犬|[PNG](../../public/assets/dogs/full/finnish-spitz-full.png)|[JSON](records/B036-full-v01.json)|PASS|

[合版 round3-b02-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b02-dpl-ill-1.2-v01-paper.png)

[合版 round3-b02-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b02-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: giant Great Dane/Bernese/Saint Bernard, slim Whippet, curled Bichon and spitz profiles remain distinct; no obvious clipped ear tips, paws or tails. Eskimo/Samoyed family resemblance retained as a final human comparison point; no human approval assigned.
