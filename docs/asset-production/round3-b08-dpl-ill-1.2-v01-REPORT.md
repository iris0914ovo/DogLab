# round3-b08-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存11张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号424项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B096|魏玛犬|[PNG](../../public/assets/dogs/full/weimaraner-full.png)|[JSON](records/B096-full-v01.json)|PASS|
|B097|维兹拉犬|[PNG](../../public/assets/dogs/full/vizsla-full.png)|[JSON](records/B097-full-v01.json)|PASS|
|B098|英国指示犬|[PNG](../../public/assets/dogs/full/english-pointer-full.png)|[JSON](records/B098-full-v01.json)|PASS|
|B099|英国塞特犬|[PNG](../../public/assets/dogs/full/english-setter-full.png)|[JSON](records/B099-full-v01.json)|PASS|
|B100|爱尔兰塞特犬|[PNG](../../public/assets/dogs/full/irish-setter-full.png)|[JSON](records/B100-full-v01.json)|PASS|
|B101|戈登塞特犬|[PNG](../../public/assets/dogs/full/gordon-setter-full.png)|[JSON](records/B101-full-v01.json)|PASS|
|B102|布列塔尼犬|[PNG](../../public/assets/dogs/full/brittany-full.png)|[JSON](records/B102-full-v01.json)|PASS|
|B103|英国斗牛犬|[PNG](../../public/assets/dogs/full/bulldog-full.png)|[JSON](records/B103-full-v01.json)|PASS|
|B105|波士顿梗|[PNG](../../public/assets/dogs/full/boston-terrier-full.png)|[JSON](records/B105-full-v01.json)|PASS|
|B106|巴哥犬|[PNG](../../public/assets/dogs/full/pug-full.png)|[JSON](records/B106-full-v01.json)|PASS|
|B107|北京犬|[PNG](../../public/assets/dogs/full/pekingese-full.png)|[JSON](records/B107-full-v01.json)|PASS|

[合版 round3-b08-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b08-dpl-ill-1.2-v01-paper.png)

[合版 round3-b08-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b08-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: pointer and setter coats/body proportions distinguishable; Bulldog/Boston/Pug/Pekingese retain separate ear, head and body profiles with visible noses and complete paws/tails. No obvious clipping. Short-muzzle proportions and skin folds remain final human welfare/anatomy review points; no clinical health inference or automatic approval.
