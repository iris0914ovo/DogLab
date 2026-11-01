# round3-b05-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存11张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号348项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B061|比利时特伏丹犬|[PNG](../../public/assets/dogs/full/belgian-tervuren-full.png)|[JSON](records/B061-full-v01.json)|PASS|
|B062|比利时格罗安达犬|[PNG](../../public/assets/dogs/full/belgian-groenendael-full.png)|[JSON](records/B062-full-v01.json)|PASS|
|B063|比利时拉肯努阿犬|[PNG](../../public/assets/dogs/full/belgian-laekenois-full.png)|[JSON](records/B063-full-v01.json)|PASS|
|B064|粗毛柯利犬|[PNG](../../public/assets/dogs/full/rough-collie-full.png)|[JSON](records/B064-full-v01.json)|PASS|
|B065|短毛柯利犬|[PNG](../../public/assets/dogs/full/smooth-collie-full.png)|[JSON](records/B065-full-v01.json)|PASS|
|B066|古代英国牧羊犬|[PNG](../../public/assets/dogs/full/old-english-sheepdog-full.png)|[JSON](records/B066-full-v01.json)|PASS|
|B067|长须柯利犬|[PNG](../../public/assets/dogs/full/bearded-collie-full.png)|[JSON](records/B067-full-v01.json)|PASS|
|B068|布里牧羊犬|[PNG](../../public/assets/dogs/full/briard-full.png)|[JSON](records/B068-full-v01.json)|PASS|
|B069|波利犬|[PNG](../../public/assets/dogs/full/puli-full.png)|[JSON](records/B069-full-v01.json)|PASS|
|B071|穆迪犬|[PNG](../../public/assets/dogs/full/mudi-full.png)|[JSON](records/B071-full-v01.json)|PASS|
|B072|普米犬|[PNG](../../public/assets/dogs/full/pumi-full.png)|[JSON](records/B072-full-v01.json)|PASS|

[合版 round3-b05-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b05-dpl-ill-1.2-v01-paper.png)

[合版 round3-b05-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b05-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected actual paper contact sheet: long narrow Collie heads, heavier Old English Sheepdog, Bearded/Briard furnishings, black corded Puli, short-face-hair wavy Mudi and folded-tip Pumi remain distinguishable. No obvious ear/tail/paw clipping. Fine ear carriage and wolf-claw anatomy hidden under coats require final human close review; no automatic approval.
