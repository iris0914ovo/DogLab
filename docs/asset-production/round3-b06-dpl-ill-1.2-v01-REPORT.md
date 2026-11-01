# round3-b06-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存11张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号320项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B073|波兰低地牧羊犬|[PNG](../../public/assets/dogs/full/polish-lowland-sheepdog-full.png)|[JSON](records/B073-full-v01.json)|PASS|
|B074|伯格马斯科牧羊犬|[PNG](../../public/assets/dogs/full/bergamasco-sheepdog-full.png)|[JSON](records/B074-full-v01.json)|PASS|
|B075|博斯牧羊犬|[PNG](../../public/assets/dogs/full/beauceron-full.png)|[JSON](records/B075-full-v01.json)|PASS|
|B076|卡迪根威尔士柯基犬|[PNG](../../public/assets/dogs/full/cardigan-welsh-corgi-full.png)|[JSON](records/B076-full-v01.json)|PASS|
|B077|白色瑞士牧羊犬|[PNG](../../public/assets/dogs/full/white-swiss-shepherd-dog-full.png)|[JSON](records/B077-full-v01.json)|PASS|
|B079|美国可卡犬|[PNG](../../public/assets/dogs/full/american-cocker-spaniel-full.png)|[JSON](records/B079-full-v01.json)|PASS|
|B080|英国史宾格犬|[PNG](../../public/assets/dogs/full/english-springer-spaniel-full.png)|[JSON](records/B080-full-v01.json)|PASS|
|B081|威尔士史宾格犬|[PNG](../../public/assets/dogs/full/welsh-springer-spaniel-full.png)|[JSON](records/B081-full-v01.json)|PASS|
|B082|克伦伯猎犬|[PNG](../../public/assets/dogs/full/clumber-spaniel-full.png)|[JSON](records/B082-full-v01.json)|PASS|
|B083|苏塞克斯猎犬|[PNG](../../public/assets/dogs/full/sussex-spaniel-full.png)|[JSON](records/B083-full-v01.json)|PASS|
|B084|田野猎犬|[PNG](../../public/assets/dogs/full/field-spaniel-full.png)|[JSON](records/B084-full-v01.json)|PASS|

[合版 round3-b06-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b06-dpl-ill-1.2-v01-paper.png)

[合版 round3-b06-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b06-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: Bergamasco flattened mats differ from cords and straight coats; Beauceron short coat, Cardigan broad ears/long tail, white shepherd and spaniel body/ear profiles are visible. No obvious missing ear/tail/paws. Closely related English/Welsh Springer and other spaniels retain natural family resemblance, flagged for final human comparison; long coat fine anatomy remains pending.
