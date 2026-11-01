# 第三轮102种全身图：最终生产与远程验证汇总

当前状态：第三轮 **102/102** 个犬种已实际生成、保存、基础技术检查、AI合版检视及GitHub同步；全项目共 **120张正式全身PNG**。当前固定风格DPL-ILL-1.2。前两轮18张全身图字节未改；32种人格肖像为0张；未开发网站或部署。

## 生产与QC结果

9批，前三批各12张、后六批各11张，102个Breed ID/slug与BREED_DATA一一对应；每种独立Prompt、独立真实图像工具调用。正式PNG为1024×1024 RGBA、背景真实透明、主体核心不透明、边缘自然抗锯齿，等比处理且保留安全边。原始母图、Prompt版本及SHA256、实际工具路径/名称、处理参数与QC均保存；工具未暴露模型ID时记null，不伪造。

本轮实际调用图像工具104次：101种各一次，B055墨西哥无毛犬3次。B055前两个站姿候选因与秘鲁无毛犬过近而未采纳，原始图、候选PNG、Prompt与失败原因均归档；当前正式文件为坐姿v03，技术检查与AI检视已完成，不覆盖前两轮图片。没有保存失败后重复生成，没有未解决技术失败，没有用SVG、占位图或随机网图替代。

全项目120张当前正式文件及其像素哈希均不重复；低分辨率轮廓相似信号在批次JSON保留，不等于已判定重复。相近犬种不能只靠哈希鉴定，以下仍需最终人工比较：白色尖嘴家族（如B034/B044/B045/B049）、伦德B038多趾、亚洲尖嘴与无毛犬细节、相近史宾格/猎犬、B088/B089卷毛犬、B113/B114梗犬、短口吻犬口鼻比例及长毛遮挡的细部。全部102张仍待用户最终人工复核，不自动标为APPROVED。

## 九批提交、全部合版与报告

| 批次 | 张数 | 已验证生产提交（完整哈希） | 全部预览合版 | 质检报告 | 远程证据 |
|---|---:|---|---|---|---|
| 01 | 12 | [3f70176e14f9eba231ae9bae495420efe71ee752](https://github.com/iris0914ovo/DogLab/commit/3f70176e14f9eba231ae9bae495420efe71ee752) | [paper](../../public/assets/dogs/review/round3-b01-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b01-dpl-ill-1.2-v01-ink.png) | [报告](round3-b01-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b01-dpl-ill-1.2-v01.json) |
| 02 | 12 | [eb7392f7f5a7afe52ade5a5fdb114d3b7515557e](https://github.com/iris0914ovo/DogLab/commit/eb7392f7f5a7afe52ade5a5fdb114d3b7515557e) | [paper](../../public/assets/dogs/review/round3-b02-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b02-dpl-ill-1.2-v01-ink.png) | [报告](round3-b02-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b02-dpl-ill-1.2-v01.json) |
| 03 | 12 | [3752d43741f2f225e58ebbff23dfc50c36e55144](https://github.com/iris0914ovo/DogLab/commit/3752d43741f2f225e58ebbff23dfc50c36e55144) | [paper](../../public/assets/dogs/review/round3-b03-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b03-dpl-ill-1.2-v01-ink.png) | [报告](round3-b03-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b03-dpl-ill-1.2-v01.json) |
| 04 | 11 | [2cb692572b007206064a489a92bd6e6f4c5c29eb](https://github.com/iris0914ovo/DogLab/commit/2cb692572b007206064a489a92bd6e6f4c5c29eb) | [paper](../../public/assets/dogs/review/round3-b04-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b04-dpl-ill-1.2-v01-ink.png) | [报告](round3-b04-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b04-dpl-ill-1.2-v01.json) |
| 05 | 11 | [2280fe7364848052da524998a57bf06fe468afa9](https://github.com/iris0914ovo/DogLab/commit/2280fe7364848052da524998a57bf06fe468afa9) | [paper](../../public/assets/dogs/review/round3-b05-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b05-dpl-ill-1.2-v01-ink.png) | [报告](round3-b05-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b05-dpl-ill-1.2-v01.json) |
| 06 | 11 | [db63d5e3030cf3bc2ba672c2165ee348a806cf6c](https://github.com/iris0914ovo/DogLab/commit/db63d5e3030cf3bc2ba672c2165ee348a806cf6c) | [paper](../../public/assets/dogs/review/round3-b06-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b06-dpl-ill-1.2-v01-ink.png) | [报告](round3-b06-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b06-dpl-ill-1.2-v01.json) |
| 07 | 11 | [c1e044db27ce38ae2dca4311644d914814fd9589](https://github.com/iris0914ovo/DogLab/commit/c1e044db27ce38ae2dca4311644d914814fd9589) | [paper](../../public/assets/dogs/review/round3-b07-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b07-dpl-ill-1.2-v01-ink.png) | [报告](round3-b07-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b07-dpl-ill-1.2-v01.json) |
| 08 | 11 | [0c6bf30678e7bfb7ea5ddb69e825ffc4291692ad](https://github.com/iris0914ovo/DogLab/commit/0c6bf30678e7bfb7ea5ddb69e825ffc4291692ad) | [paper](../../public/assets/dogs/review/round3-b08-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b08-dpl-ill-1.2-v01-ink.png) | [报告](round3-b08-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b08-dpl-ill-1.2-v01.json) |
| 09 | 11 | [1327d4728cccf80a5a4db91e8bec677f9f95c4ee](https://github.com/iris0914ovo/DogLab/commit/1327d4728cccf80a5a4db91e8bec677f9f95c4ee) | [paper](../../public/assets/dogs/review/round3-b09-dpl-ill-1.2-v01-paper.png) / [ink](../../public/assets/dogs/review/round3-b09-dpl-ill-1.2-v01-ink.png) | [报告](round3-b09-dpl-ill-1.2-v01-REPORT.md) | [JSON](verification/round3-b09-dpl-ill-1.2-v01.json) |

每批均正常push到iris0914ovo/DogLab的work，并在独立Git对象库从GitHub读取该批当前正式PNG、原图、Prompt和合版核对SHA256及实际PNG解码；每批报告与元数据也读取比较。最终又对远程全部120张正式PNG做完整SHA256与RGBA/1024解码检查，结果通过，详见 [最终120图验证](verification/round3-final-120.json)。同时确认28个此前PNG（其中包括前两轮18张正式图）未变，main仍为e885330cda4018c7ac216eeb4351a947fbd65284，无强制推送。

## 文件入口与停止范围

- [全部120种正式PNG](../../public/assets/dogs/full/)
- [资产清单](../ASSET_MANIFEST.md)
- [逐图生产记录](records/)
- [原始图与Prompt](../../artifacts/illustrations/)
- [当前插画规范](../ILLUSTRATION_GUIDE.md)
- [审核历史与授权](../ILLUSTRATION_REVIEW.md)

清单的正式人格聚合状态仍受缺少肖像影响而为PLANNED；这不表示其全身图未制作，实际全身文件与逐文件GENERATED/APPROVED状态分别记录。前两轮全身文件APPROVED，第三轮102张GENERATED且待最终人工审核。

本轮全部102张完成后停止。不得据此启动32张肖像、网站开发或GitHub Pages部署。
