# round3-b07-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存11张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号443项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B085|爱尔兰水猎犬|[PNG](../../public/assets/dogs/full/irish-water-spaniel-full.png)|[JSON](records/B085-full-v01.json)|PASS|
|B086|美国水猎犬|[PNG](../../public/assets/dogs/full/american-water-spaniel-full.png)|[JSON](records/B086-full-v01.json)|PASS|
|B087|葡萄牙水犬|[PNG](../../public/assets/dogs/full/portuguese-water-dog-full.png)|[JSON](records/B087-full-v01.json)|PASS|
|B088|西班牙水犬|[PNG](../../public/assets/dogs/full/spanish-water-dog-full.png)|[JSON](records/B088-full-v01.json)|PASS|
|B089|罗马涅水犬|[PNG](../../public/assets/dogs/full/lagotto-romagnolo-full.png)|[JSON](records/B089-full-v01.json)|PASS|
|B090|切萨皮克湾寻回犬|[PNG](../../public/assets/dogs/full/chesapeake-bay-retriever-full.png)|[JSON](records/B090-full-v01.json)|PASS|
|B091|平毛寻回犬|[PNG](../../public/assets/dogs/full/flat-coated-retriever-full.png)|[JSON](records/B091-full-v01.json)|PASS|
|B092|卷毛寻回犬|[PNG](../../public/assets/dogs/full/curly-coated-retriever-full.png)|[JSON](records/B092-full-v01.json)|PASS|
|B093|新斯科舍诱鸭寻回犬|[PNG](../../public/assets/dogs/full/nova-scotia-duck-tolling-retriever-full.png)|[JSON](records/B093-full-v01.json)|PASS|
|B094|德国短毛指示犬|[PNG](../../public/assets/dogs/full/german-shorthaired-pointer-full.png)|[JSON](records/B094-full-v01.json)|PASS|
|B095|德国刚毛指示犬|[PNG](../../public/assets/dogs/full/german-wirehaired-pointer-full.png)|[JSON](records/B095-full-v01.json)|PASS|

[合版 round3-b07-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b07-dpl-ill-1.2-v01-paper.png)

[合版 round3-b07-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b07-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: Irish Water Spaniel short-haired tail, wavy American/Portuguese coats, flat versus tightly curled retriever coats and short versus wire-haired pointers visible; no obvious ear/tail/paw clipping. Spanish Water Dog/Lagotto similar curly family profiles flagged for final human head/body comparison; automatic QC is not breed certification or approval.
