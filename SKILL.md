---
name: latex-defense-ppt-skill
description: >
  Create polished undergraduate or graduate thesis defense PPTX slides from a LaTeX thesis directory and a school/template PPTX.
  Use when the user asks for 本科毕设答辩PPT, 学位论文答辩PPT, LaTeX论文转PPT, academic defense slides, or wants to generate, refine, or audit a high-quality academic defense deck from a thesis and template.
  The workflow emphasizes thesis-accurate narrative, template-faithful visual style, strict alignment, figure reuse, concise paragraph analysis, evidence-driven experiment slides, and automated PPTX QA.
---

# LaTeX Defense PPT Skill

Turn a LaTeX thesis directory and a PPTX template into a high-quality defense presentation.

## Inputs

Required:
- LaTeX thesis directory, preferably with a main `.tex`, chapter `.tex` files, and figure folders.
- PPTX template from the school/lab, or a clear visual reference.

Optional:
- Existing generated figures or AI-image assets.
- Defense duration, target slide count, school/department/author metadata.
- User notes on mandatory or forbidden figures.

## Core Workflow

1. Inspect the thesis structure.
   - Locate the main `.tex`, chapter files, abstract, metadata, and image folders.
   - Extract thesis title, author, supervisor, institution, research object, methods, experiments, and conclusions.
   - Use `rg` first. Quote local file paths and lines when reporting evidence.

2. Build the narrative before designing pages.
   - For a 10-minute undergraduate defense, target 20-22 slides unless the user says otherwise.
   - Prefer this arc: cover, agenda, background/data, problem, data sources/objects, technical route, method gap, factor system, screening, model innovation, model architecture, key mechanism, experiment design, core results, robustness/application, summary, thanks.
   - Keep the thesis logic intact. Do not invent claims beyond the source.
   - For new projects, first present a compact outline for user confirmation before generating the deck; after confirmation, save the working outline.

3. Use the template as the visual source of truth.
   - Reuse slide size, background, school logo/seal, color style, and footer feel.
   - It is acceptable to rebuild slides with editable PowerPoint objects instead of copying complex template elements.
   - If the template cannot be programmatically used, create a high-fidelity approximation.
   - When a template PPTX exists, run `scripts/analyze_template.py` or manually inspect equivalent style signals before creating the deck.

4. Reuse thesis figures first.
   - Use original thesis figures for model architecture, experiment plots, ablation, robustness, and backtest results.
   - Use AI image generation only for missing framework/process diagrams that the thesis does not already provide.
   - If image generation fails, create a deterministic fallback layout rather than blocking delivery.

5. Write slide text as concise academic paragraphs.
   - Avoid tag-only lists such as “多源异构 / 非线性波动 / 结构切换”.
   - Use short paragraph explanations that answer: what was done, what result was observed, what conclusion it proves.
   - Highlight only the most important numbers or claims in a deep red bold style.

6. Enforce layout rigor.
   - Use a fixed content grid, consistent title bar, footer, image frames, conclusion bars, and column boundaries.
   - Align text boxes, picture frames, cards, and conclusion bars by frame edges, not by the visual edges of cropped images.
   - Avoid large empty cards. Prefer compact analysis card + note card + keyword strip + evidence mini-cards.

7. Run QA before final response.
   - Check slide count, page size, out-of-bounds objects, tiny text boxes, bullet glyphs, text-picture overlaps, and font-size drift.
   - Generate visual previews/contact sheet when possible; run image-based visual QA if preview PNGs are available.
   - Fix visible alignment, empty-space, overlap, or unreadable text issues before reporting completion.

## Reference Files

Load only what is needed:
- `references/workflow.md`: full production workflow from LaTeX to final PPTX.
- `references/content-rules.md`: defense narrative and wording rules.
- `references/layout-rules.md`: alignment, typography, and page design rules.
- `references/beamer-academic-distillation.md`: condensed reusable ideas from the beamer-academic skill, adapted for PPTX/template workflows.
- `references/agent-playbook.md`: multi-agent role split and review loop for high-stakes deck production.
- `references/quality-checklist.md`: final QA checklist distilled from this project.

## Bundled Scripts

- `scripts/pptx_qa.py`: structural PPTX checks.
- `scripts/analyze_template.py`: summarize reusable style signals from a PPTX template.
- `scripts/render_contact_sheet.py`: render slide thumbnails and a contact sheet with QuickLook, LibreOffice, or PowerPoint.
- `scripts/visual_qa.py`: image-based checks for empty pages, large margins, and center drift from rendered previews.

Typical QA:

```bash
python3 latex-defense-ppt-skill/scripts/analyze_template.py template.pptx --json-out tmp/template_style.json
python3 latex-defense-ppt-skill/scripts/pptx_qa.py output.pptx --expected-slides 22 --warn-only
python3 latex-defense-ppt-skill/scripts/render_contact_sheet.py output.pptx --out-dir tmp/ppt_preview
python3 latex-defense-ppt-skill/scripts/visual_qa.py tmp/ppt_preview/previews --warn-only
```

## Final Response

Report:
- Output PPTX path.
- Slide count.
- Major content/design changes.
- QA results.
- Any unresolved caveats, such as failed image-generation API calls.
