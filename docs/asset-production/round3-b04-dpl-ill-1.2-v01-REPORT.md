# round3-b04-dpl-ill-1.2-v01 生产与基础质检报告

实际独立生成并保存11张全身PNG，全部1024×1024 RGBA，真实透明背景，主体核心不透明，保留边缘抗锯齿，等比缩放、安全边至少102px。保留原始母图与Prompt/SHA256、工具、处理参数。工具未暴露模型ID时如实为null，不伪造。原生Alpha微量残留与近不透明值按既定处理器规范化，原图不改写；raw_qc保留源图触边风险。

跨所有已生产图片的文件和像素SHA256无重复；本批关联的低分辨率轮廓相似信号182项保存在批次JSON中，不等于重复图。自动QC不保证犬种解剖或人工批准，需要合版AI检查和最终人工复核。

|ID|犬种|PNG|记录|基础QC|
|---|---|---|---|---|
|B049|纪州犬|[PNG](../../public/assets/dogs/full/kishu-full.png)|[JSON](records/B049-full-v01.json)|PASS|
|B050|甲斐犬|[PNG](../../public/assets/dogs/full/kai-ken-full.png)|[JSON](records/B050-full-v01.json)|PASS|
|B051|韩国珍岛犬|[PNG](../../public/assets/dogs/full/korea-jindo-dog-full.png)|[JSON](records/B051-full-v01.json)|PASS|
|B052|迦南犬|[PNG](../../public/assets/dogs/full/canaan-dog-full.png)|[JSON](records/B052-full-v01.json)|PASS|
|B053|泰国脊背犬|[PNG](../../public/assets/dogs/full/thai-ridgeback-full.png)|[JSON](records/B053-full-v01.json)|PASS|
|B055|墨西哥无毛犬|[PNG](../../public/assets/dogs/full/xoloitzcuintli-full.png)|[JSON](records/B055-full-v03.json)|PASS|
|B056|葡萄牙波登可犬|[PNG](../../public/assets/dogs/full/portuguese-podengo-full.png)|[JSON](records/B056-full-v01.json)|PASS|
|B057|伊比赞猎犬|[PNG](../../public/assets/dogs/full/ibizan-hound-full.png)|[JSON](records/B057-full-v01.json)|PASS|
|B058|法老王猎犬|[PNG](../../public/assets/dogs/full/pharaoh-hound-full.png)|[JSON](records/B058-full-v01.json)|PASS|
|B059|澳大利亚牧牛犬|[PNG](../../public/assets/dogs/full/australian-cattle-dog-full.png)|[JSON](records/B059-full-v01.json)|PASS|
|B060|比利时马林诺斯犬|[PNG](../../public/assets/dogs/full/belgian-malinois-full.png)|[JSON](records/B060-full-v01.json)|PASS|

[合版 round3-b04-dpl-ill-1.2-v01-paper](../../public/assets/dogs/review/round3-b04-dpl-ill-1.2-v01-paper.png)

[合版 round3-b04-dpl-ill-1.2-v01-ink](../../public/assets/dogs/review/round3-b04-dpl-ill-1.2-v01-ink.png)

每批push work后独立临时Git仓库抓取并读取PNG blob核验SHA256和解码。实际远程验证证据保存于verification同名JSON。未验证前不声称远程完成。

AI合版检视（不等于人工批准）：AI inspected paper contact sheet and revised Xolo independently: B055 v01/v02 rejected for excessive standing-pose similarity to Peruvian hairless; v03 natural sitting pose retains full ears, feet and tail and is current. Both prior candidates archived. Other breeds show visible coat/ear/skeleton differences; Asian spitz family resemblance and Thai dorsal ridge visibility remain final human review points. No human approval assigned.
