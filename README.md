# DOG PERSONA LAB｜犬格研究所

一个原创的娱乐性狗狗人格测试与犬种图鉴项目。通过 24 道生活情境题生成八维行为倾向，与 32 种原创犬格匹配，并提供 120 种犬种图鉴。无需登录，计划在浏览器本地处理答题与结果。

视觉方向为 Editorial Design：像一本现代互动杂志，重视字体、留白、色彩、原创插画及排版节奏，不采用 SaaS Dashboard、Bento Grid 或满屏圆角卡片模板，不默认使用 shadcn/ui、Ant Design、MUI。

## 产品文档

| 文档 | 内容 |
|---|---|
| [PRD V1.0](docs/PRD.md) | 用户提供的完整产品需求原文 |
| [正式题库](docs/QUESTION_BANK.md) | 24 道全新原创题目、维度、选项及计分 |
| [人格数据](docs/PERSONALITY_DATA.md) | 32 种犬格、八维向量、独立文案及匹配补充约定 |
| [犬种图鉴](docs/BREED_DATA.md) | 120 条唯一犬种记录、32 种正式犬格关联及 88 条普通图鉴拟人旁白 |
| [内容规范](docs/CONTENT_GUIDELINES.md) | 语气、创作规则、事实边界、隐私与内容审查 |
| [视觉系统](docs/DESIGN_SYSTEM.md) | 品牌、色彩、字体、页面网格、响应式与插画规范 |

## Phase 2 视觉交付

- [插画生产规范](docs/ILLUSTRATION_GUIDE.md)
- [120 种犬种资产索引](docs/ASSET_MANIFEST.md)
- [第一批六份完整角色 Prompt](docs/FIRST_BATCH_PROMPTS.md)
- [品牌标志与使用说明](docs/BRAND_IDENTITY.md)
- [主标志 SVG](public/assets/brand/logo-primary.svg)、[反白标志 SVG](public/assets/brand/logo-reverse.svg)、[辅助符号 SVG](public/assets/brand/symbol.svg)

## 当前开发阶段

当前处于 **Phase 2：原创视觉系统与角色设计，等待视觉审核**。Phase 1 文档已提交并推送；本批建立插画生产规范、120 种犬种素材计划、原创 SVG 品牌提案与六份角色 Prompt。首批六张真实全身候选已自动生成、保存并进行基础技术质检，另有六张合版预览，全部待集中视觉审核；肖像未制作，资产聚合状态仍按最低进度保持 PLANNED。品牌提案尚未获用户视觉批准。仓库未初始化 React、Vite 或 TypeScript，没有网站页面、测试算法或 Pages 部署配置。审核前不进入 Phase 3，也不批量生成其余 114 种插画。

| 阶段 | 交付范围 |
|---|---|
| Phase 0 | GitHub 仓库检查 |
| Phase 1 | 产品需求和内容文档 |
| Phase 2 | 原创视觉系统和角色插画 |
| Phase 3 | React 项目初始化和基础页面 |
| Phase 4 | 24 道题和八维计分 |
| Phase 5 | 32 种犬格结果页 |
| Phase 6 | 120 种犬种图鉴 |
| Phase 7 | 分享和图片导出 |
| Phase 8 | 功能测试和视觉验收 |
| Phase 9 | GitHub Pages 部署 |

计划技术栈：React + TypeScript + Vite、原生 CSS、SVG、Hash 路由、localStorage、html-to-image；计划托管 GitHub Pages。每阶段检查后再推进，尚未实现的能力不作为当前功能宣传。

## 数据约定与限制

固定维度顺序为：社交续航、边界雷达、情绪回弹、表达外放、探索欲、行动启动、秩序需求、关系修复。题目分值仅供开发，不在用户界面显示。原始 PRD 不改写，补充决定记录在对应文档。犬格是人工创作模型，未经过心理测量验证；犬种形态介绍尚需上线前逐条来源核验。

犬格研究所是一款娱乐性人格测试。测试结果由用户对生活情境的选择生成，用于趣味性人格表达和社交分享，不属于专业心理测评或心理诊断。犬格人格是对犬种形象的拟人化创作，不代表所有真实犬只的个体性格。

## 首批六犬实际生产

[生产与质检报告](docs/asset-production/ROUND1_REPORT.md) · [六张合版](public/assets/dogs/review/) · [逐图记录](docs/asset-production/records/)

当前会话使用 image_gen__imagegen 生成并自动获取本地真实 PNG，未调用独立 API。模型未暴露具体型号，记录为 null。原始母图与处理后的透明 PNG 均保留，不代表最终人工批准。
