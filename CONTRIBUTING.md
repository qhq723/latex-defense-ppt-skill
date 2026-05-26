# 贡献指南

感谢你愿意改进这个 skill。它的目标是帮助 Codex / Claude Code 从 LaTeX 论文和 PPTX 模板生成高质量答辩 PPT。

## 贡献方向

- 改进论文理解、素材提取、页面设计和 QA 流程。
- 增强跨平台预览导出能力。
- 增强模板分析、视觉检查和字体/对齐检查。
- 补充更清晰的中文说明和提示词。
- 修复脚本在不同系统或不同 PPTX 文件上的兼容问题。

## 不建议提交

- 真实论文、学校内部模板、学生个人信息。
- 未授权的学校 logo、商业字体、图片素材。
- 针对单个私有论文的硬编码规则。
- 大体积生成产物，如 `.pptx`、预览图片、临时目录。

## 本地检查

```bash
python3 -m py_compile scripts/*.py
python3 scripts/analyze_template.py your-template.pptx --json-out tmp/template_style.json
python3 scripts/pptx_qa.py your-deck.pptx --expected-slides 22 --warn-only
python3 scripts/render_contact_sheet.py your-deck.pptx --out-dir tmp/ppt_preview
python3 scripts/visual_qa.py tmp/ppt_preview/previews --warn-only
```

如果没有真实模板或 PPTX，可以至少运行 Python 语法检查。

## 文档原则

- `SKILL.md` 保持简洁，只放触发后必须立刻知道的流程。
- 详细规则放在 `references/`，让 agent 按需读取。
- 脚本要优先稳定、可解释，避免只适配某一份 PPT。
