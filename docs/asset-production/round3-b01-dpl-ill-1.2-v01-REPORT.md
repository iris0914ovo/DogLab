# round3-b01-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存12张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号94项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B006|拉布拉多寻回犬|[PNG](../../public/assets/dogs/full/labrador-retriever-full.png)|[JSON](records/B006-full-v01.json)|PASS|
|B008|德国牧羊犬|[PNG](../../public/assets/dogs/full/german-shepherd-dog-full.png)|[JSON](records/B008-full-v01.json)|PASS|
|B009|萨摩耶犬|[PNG](../../public/assets/dogs/full/samoyed-full.png)|[JSON](records/B009-full-v01.json)|PASS|
|B010|秋田犬|[PNG](../../public/assets/dogs/full/akita-full.png)|[JSON](records/B010-full-v01.json)|PASS|
|B011|比格犬|[PNG](../../public/assets/dogs/full/beagle-full.png)|[JSON](records/B011-full-v01.json)|PASS|
|B013|杰克罗素梗|[PNG](../../public/assets/dogs/full/jack-russell-terrier-full.png)|[JSON](records/B013-full-v01.json)|PASS|
|B014|西高地白梗|[PNG](../../public/assets/dogs/full/west-highland-white-terrier-full.png)|[JSON](records/B014-full-v01.json)|PASS|
|B016|喜乐蒂牧羊犬|[PNG](../../public/assets/dogs/full/shetland-sheepdog-full.png)|[JSON](records/B016-full-v01.json)|PASS|
|B017|澳大利亚牧羊犬|[PNG](../../public/assets/dogs/full/australian-shepherd-full.png)|[JSON](records/B017-full-v01.json)|PASS|
|B018|杜宾犬|[PNG](../../public/assets/dogs/full/dobermann-full.png)|[JSON](records/B018-full-v01.json)|PASS|
|B019|罗威纳犬|[PNG](../../public/assets/dogs/full/rottweiler-full.png)|[JSON](records/B019-full-v01.json)|PASS|
|B020|拳师犬|[PNG](../../public/assets/dogs/full/boxer-full.png)|[JSON](records/B020-full-v01.json)|PASS|

[合版 round3-b01-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b01-dpl-ill-1.2-v01-paper.png)

[合版 round3-b01-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b01-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。
