# LaTeX 论文答辩 PPT Skill

一个面向 Codex / Claude Code 的本科、硕士、博士论文答辩 PPT 自动制作 skill。输入一份 LaTeX 论文目录和一份学校/课题组 PPTX 模板，它会先理解论文研究内容，再生成结构清晰、图文并茂、格式经过质检的答辩 PPTX。

这份 skill 沉淀自一次完整的本科毕设答辩 PPT 制作流程：论文理解、模板仿制、22 页讲述逻辑设计、论文配图复用、框架图补充、多轮排版精修、实验页文字打磨、自动化 QA 与预览复查。

## 能做什么

- 从 LaTeX 论文目录中梳理题目、研究对象、数据来源、方法、实验与结论。
- 复用学校或课题组提供的 `pptx` 模板，包括校徽、背景、页脚、主色调和标题风格。
- 优先使用论文中的原始插图，避免低质量截图和无关装饰图。
- 按 10 分钟答辩节奏生成约 20-22 页 PPT，也可按用户要求调整页数。
- 自动设计封面、目录、研究背景、数据来源、技术路线、模型设计、实验结果、回测验证、总结展望、致谢页。
- 将实验页写成“结果现象 -> 证明结论”的凝练学术表达，而不是简单堆图或堆关键词。
- 对齐文本框、图片框、分析卡、页脚和结论条，尽量避免错位、重叠、留白过大、字号漂移等问题。
- 运行结构 QA，并可用 QuickLook、LibreOffice 或 PowerPoint 生成缩略图预览 contact sheet 方便人工复查。

## 已沉淀的 PPT 制作要求

这部分来自实际制作过程中的多轮反馈，是本 skill 的核心审美和质量标准：

- **先理解论文，再做 PPT**：不能直接套通用模板，要准确复现论文的研究思路、实验链条和创新逻辑。
- **模板优先**：整体风格必须服从用户提供的学校/学院模板；可重建复杂元素，但校徽、标志、主色、页脚和版心要保持一致。
- **页数服务于讲述**：10 分钟本科答辩建议 20-22 页，不为了页数强行压缩关键逻辑。
- **必须讲清数据**：数据来源、时间范围、频率对齐、研究标的和异质性选择依据需要单独说明，不能跳过。
- **论文原图优先**：模型结构、实验结果、消融、回测等图尽量使用论文已有图；只有缺少框架图/流程图时才补充生成图。
- **少用空泛标签**：避免“多源异构 / 非线性波动 / 结构切换”这类标签堆叠，改用小段落解释研究动机、方法作用和实验证据。
- **实验页要有结论解释**：每张结果页都要说明“什么结果证明了什么结论”，不能只展示图表。
- **重点适度高亮**：核心数值、最优结果、关键结论可用深红色加粗，但每页只突出少量重点。
- **严格对齐**：标题、校徽、图片、文本框、分析卡、结论条、页脚都要按统一网格对齐；封面和致谢页尤其要做中心轴对齐。
- **避免大面积空白**：大的分析框里不能只有两三行字；优先使用紧凑分析卡、说明卡、关键词条、证据小卡组合。
- **统一字体字号**：同一级别文本使用一致或近似一致的字号，如标题、正文、注释、证据卡、页脚、结论条。
- **复查后交付**：生成后必须跑 QA，尽量生成预览图，并人工检查封面、目录、模型页、实验页、总结页和致谢页。

## 借鉴并凝练的 beamer-academic 思路

制作这份 skill 时参考并吸收了 `beamer-academic` 的成熟流程，但做了 PPTX 模板化改造。已经沉淀到 `references/beamer-academic-distillation.md` 中，主要包括：

- 分阶段流程：论文理解 -> 素材提取 -> 图表目录 -> 大纲确认 -> 页面分配 -> 生成 -> QA -> 迭代。
- 先建素材目录，再决定哪些图进入 PPT，避免遗漏关键论文图。
- PPT 结构以论文原有章节和论证逻辑为主，而不是套用泛泛的论文汇报模板。
- 生成前尽量给出页级大纲，让用户确认每页标题、版式、目的和图源。
- 控制版式节奏，避免连续多页同一种结构。
- 反 AI 味写作：少用项目符号，多用凝练段落、证据卡和结论条。
- 迭代时把“这页不好看”“太空了”等反馈转成可执行的版式修复方案。

## 要求落地位置

不同文件承担不同职责：

- `SKILL.md`：agent 触发后首先读取的核心流程，规定输入、总体工作流、模板优先、论文原图优先、段落化写作和最终 QA。
- `references/workflow.md`：完整生产流程，包括论文检索命令、素材目录、10 分钟 21-22 页推荐结构、迭代修复方式。
- `references/content-rules.md`：内容写作规则，重点约束数据页、方法不足页、实验结论解释、深红色重点高亮。
- `references/layout-rules.md`：排版规范，约束固定网格、封面/致谢居中、图文页结构、字号体系、留白处理和禁止版式。
- `references/beamer-academic-distillation.md`：从 `beamer-academic` 凝练出的阶段化流程、大纲确认、版式节奏、反 AI 写作和图片提取规则。
- `references/agent-playbook.md`：多 agent 协作手册，规定论文理解、内容策划、美工模板、生成、文案精修、QA 审核的分工。
- `references/quality-checklist.md`：最终人工复查清单，覆盖内容、视觉、字号、图片和自动化 QA。
- `scripts/analyze_template.py`：分析 PPTX 模板的页面尺寸、主色、字体、标题/页脚/图片位置候选。
- `scripts/pptx_qa.py`：检查页数、越界对象、极小文本框、bullet 字符、图文粗略重叠和字号分布。
- `scripts/render_contact_sheet.py`：用 QuickLook、LibreOffice 或 PowerPoint 生成缩略图总览，便于人工检查对齐、留白和整体节奏。
- `scripts/visual_qa.py`：基于缩略图检查疑似空页、大留白、中心偏移和低对比问题。

## 目录结构

```text
latex-defense-ppt-skill/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── agent-playbook.md
│   ├── beamer-academic-distillation.md
│   ├── content-rules.md
│   ├── layout-rules.md
│   ├── quality-checklist.md
│   └── workflow.md
└── scripts/
    ├── analyze_template.py
    ├── pptx_qa.py
    ├── render_contact_sheet.py
    └── visual_qa.py
```

## 安装方式

Codex 用户可以把整个目录复制到本地 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R latex-defense-ppt-skill ~/.codex/skills/
```

然后重启或新开一个 Codex 会话，在论文项目根目录中使用即可。

Claude Code 或其他支持 skill 的 agent，可以把该目录放到对应的本地 skill/plugin 目录，确保 `SKILL.md` 能被发现。

## 推荐输入

把这些文件放在同一个项目目录里最省心：

```text
your-thesis/
├── main.tex
├── chapters/
├── figures/
├── references.bib
└── 答辩模板.pptx
```

如果目录结构不同也可以，只要告诉 agent：

- LaTeX 论文目录路径
- 主 `.tex` 文件路径，如有
- PPTX 模板路径
- 答辩时长和目标页数
- 学校、学院、作者、导师等元信息
- 必须使用或禁止使用的图片

## 一句话使用提示词

```text
请使用 latex-defense-ppt-skill，读取当前目录下的 LaTeX 本科毕业论文，
并使用 答辩模板.pptx 制作一份 10 分钟左右、约 22 页的本科毕设答辩 PPT。
要求先理解论文研究内容，复用论文插图，严格套用模板风格，做好文本和图片对齐，
实验页要说明每个结果证明什么结论，最终运行 QA 并给出 PPTX 路径。
```

## 更完整的提示词模板

```text
请使用 latex-defense-ppt-skill 帮我制作论文答辩 PPT。

论文目录：/path/to/thesis
模板文件：/path/to/template.pptx
答辩时长：10 分钟
目标页数：21-22 页
学校/学院：请从模板或论文中提取，缺失时再问我
输出文件名：论文答辩.pptx

要求：
1. 先阅读 LaTeX 论文，梳理研究背景、数据来源、研究对象、方法设计、实验结果和结论。
2. 先给出页级大纲，说明每页标题、版式、内容目的和使用图片，确认后再生成。
3. 优先使用论文已有图片；只有缺少必要框架图或流程图时才补充生成图片。
4. 目录页、封面页和致谢页要美观，封面与致谢页按中心轴对齐。
5. 不要出现整页堆文字，也不要只有空泛关键词；用凝练段落、分析卡、说明卡、关键词条和证据小卡组织内容。
6. 实验结果页必须说明“观察到什么结果”和“该结果支持什么结论”。
7. 所有页面严格检查对齐、留白、字号一致性和图文重叠问题。
8. 生成后运行结构 QA，并生成预览或 contact sheet 供检查。
```

## Agent 工作流程

1. **读取论文**
   - 用 `rg --files` 找到 `.tex`、图片、表格、模板文件。
   - 抽取论文标题、作者、导师、章节结构、研究对象、数据、方法、实验、结论。
   - 必要时生成图表素材目录。

2. **设计大纲**
   - 按论文逻辑组织，而不是套通用模板。
   - 10 分钟答辩优先控制在 20-22 页。
   - 如果数据来源和研究对象很重要，单独设置一页数据说明。

3. **适配模板**
   - 运行 `scripts/analyze_template.py` 或人工总结 PPTX 模板的页面尺寸、背景、logo、主色、页脚、标题栏。
   - 内容尽量用可编辑的 PowerPoint 对象重建。

4. **生成 PPT**
   - 用 `python-pptx` 等方式生成可编辑 PPTX。
   - 使用统一网格、统一标题栏、统一页脚、统一结论条。
   - 图文页平衡图片和解释文字；无图页使用卡片、时间线、图标或证据小卡增强层次。

5. **质量检查**
   - 运行结构 QA。
   - 渲染预览或 contact sheet。
   - 人工检查关键页，发现错位、空白、重叠、文字过少或字号不统一时继续修复。

## QA 脚本

模板分析：

```bash
python3 latex-defense-ppt-skill/scripts/analyze_template.py 答辩模板.pptx --json-out tmp/template_style.json
```

结构检查：

```bash
python3 latex-defense-ppt-skill/scripts/pptx_qa.py 答辩PPT.pptx --expected-slides 22 --warn-only
```

跨平台预览缩略图：

```bash
python3 latex-defense-ppt-skill/scripts/render_contact_sheet.py 答辩PPT.pptx --out-dir tmp/ppt_preview
```

`render_contact_sheet.py` 会自动尝试后端：macOS QuickLook、LibreOffice、Windows PowerPoint。LibreOffice 后端需要安装 LibreOffice 和 `PyMuPDF`。

缩略图视觉 QA：

```bash
python3 latex-defense-ppt-skill/scripts/visual_qa.py tmp/ppt_preview/previews --warn-only
```

视觉 QA 是启发式检查，发现的留白、偏移、低对比警告需要人工判断；它的作用是提醒 agent 和使用者复查高风险页面。

## 开源说明

本 skill 是模板无关、论文无关的通用工具包，不包含任何学校 logo、私有论文内容或专有模板。用户需要提供自己的 LaTeX 论文目录和 PPTX 模板。

建议开源时保留：

- `SKILL.md`
- `references/`
- `scripts/`
- `agents/openai.yaml`
- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `requirements.txt` 或 `pyproject.toml`

不要提交真实论文、学校内部模板、学生个人信息或未授权的图片素材。
