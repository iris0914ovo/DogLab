# round3-b09-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存11张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号549项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B108|西施犬|[PNG](../../public/assets/dogs/full/shih-tzu-full.png)|[JSON](records/B108-full-v01.json)|PASS|
|B109|拉萨犬|[PNG](../../public/assets/dogs/full/lhasa-apso-full.png)|[JSON](records/B109-full-v01.json)|PASS|
|B110|马尔济斯犬|[PNG](../../public/assets/dogs/full/maltese-full.png)|[JSON](records/B110-full-v01.json)|PASS|
|B111|哈瓦那犬|[PNG](../../public/assets/dogs/full/havanese-full.png)|[JSON](records/B111-full-v01.json)|PASS|
|B112|棉花面纱犬|[PNG](../../public/assets/dogs/full/coton-de-tulear-full.png)|[JSON](records/B112-full-v01.json)|PASS|
|B113|约克夏梗|[PNG](../../public/assets/dogs/full/yorkshire-terrier-full.png)|[JSON](records/B113-full-v01.json)|PASS|
|B114|丝毛梗|[PNG](../../public/assets/dogs/full/silky-terrier-full.png)|[JSON](records/B114-full-v01.json)|PASS|
|B115|凯恩梗|[PNG](../../public/assets/dogs/full/cairn-terrier-full.png)|[JSON](records/B115-full-v01.json)|PASS|
|B117|西利哈姆梗|[PNG](../../public/assets/dogs/full/sealyham-terrier-full.png)|[JSON](records/B117-full-v01.json)|PASS|
|B118|爱尔兰梗|[PNG](../../public/assets/dogs/full/irish-terrier-full.png)|[JSON](records/B118-full-v01.json)|PASS|
|B119|万能梗|[PNG](../../public/assets/dogs/full/airedale-terrier-full.png)|[JSON](records/B119-full-v01.json)|PASS|

[合版 round3-b09-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b09-dpl-ill-1.2-v01-paper.png)

[合版 round3-b09-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b09-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: Shih Tzu/Lhasa face lengths, silky versus cotton-like white coats, erect versus folded terrier ears, Cairn/Sealyham short legs and longer Irish/Airedale profiles visible; no obvious ear/tail/paw clipping. Yorkshire/Silky and white long-coated companion similarities flagged for final human comparison; no automatic approval.
