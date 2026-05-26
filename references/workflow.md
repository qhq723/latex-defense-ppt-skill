# Workflow

## 1. Intake

Inputs:
- LaTeX thesis directory
- PPTX template
- defense duration and expected slide count
- optional required figures and generated assets

First commands:

```bash
rg --files
rg -n "\\\\(chapter|section|subsection)|数据|实验|模型|结论" *.tex
find . -maxdepth 3 -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.pptx" -o -name "*.tex" \)
```

If the user references another slide-generation skill or asks for an open-box workflow, also read `references/beamer-academic-distillation.md`. It captures the reusable parts of the beamer-academic process: material catalog, outline confirmation, layout rhythm, anti-AI writing, and guided editing.

For high-stakes production or explicit multi-agent requests, read `references/agent-playbook.md` and use the role split there as the internal review process.

## 2. Thesis Understanding

Extract:
- thesis title and metadata
- research background and pain points
- data sources, target objects, time range, sample split
- factor system or feature construction
- model architecture and modules
- baseline models
- evaluation metrics
- static, dynamic, multistep, factor contribution, ablation, robustness, and backtest conclusions
- limitations and future work

Always keep a source-backed mental map. When uncertain, search the `.tex` files again.

## 3. Figure Catalog

Create a figure inventory:

| Figure | Path | Purpose | Use in PPT |
|---|---|---|---|
| technical route | `ppt_assets/...` | roadmap | early overview |
| model architecture | `image/...` | model design | method section |
| static results | `image/...` | core result | experiment section |

Use thesis figures first. Generate new figures only for missing conceptual diagrams.

## 4. Suggested 10-Minute Structure

For 21-22 slides:

1. Cover
2. Agenda
3. Section: background/data
4. Research problem
5. Data sources and heterogeneous targets
6. Technical route
7. Method gaps and proposed response
8. Section: factor/model design
9. Multi-source factor system
10. Preprocessing and factor screening
11. Model innovation logic
12. Model architecture
13. Key mechanism
14. Section: experiments/application
15. Experiment design
16. Static prediction
17. Rolling and multistep prediction
18. Factor contribution and ablation
19. Extreme-market robustness
20. Backtest validation
21. Summary and outlook
22. Thanks

Adjust page count to match the user's defense duration. Do not compress core logic only to satisfy an arbitrary number.

Before generation, turn this into a page-level outline with `page / layout / title / purpose / figure source`. For a new user, show the outline in chat and wait for confirmation unless the user explicitly asks for fully autonomous generation.

## 5. Implementation

Reliable implementation patterns:
- Use `python-pptx` for editable PPTX generation.
- Extract template media from the PPTX package when direct template editing is hard.
- Define constants for slide size, margins, title bar, grid columns, footer, and conclusion bar.
- Use helper functions for titles, cards, picture fitting, conclusion bars, rich text, and QA.
- Fit pictures by frame. Align the frame, not the image's cropped visual content.

Template analysis:

```bash
python3 latex-defense-ppt-skill/scripts/analyze_template.py template.pptx --json-out tmp/template_style.json
```

Use the output to infer slide size, dominant colors, common font sizes, title/footer positions, and logo/picture candidates. If the script misses a template detail, inspect the template manually and encode the result as constants in the generation script.

## 6. Iteration Loop

Expected refinement loop:

1. First complete deck.
2. User reviews content and design.
3. Fix macro structure: missing data page, wrong logic, redundant diagrams.
4. Fix content: avoid shallow tags, add paragraph analysis and result-to-conclusion claims.
5. Fix visual details: alignment, empty space, title/cover/thanks centering, typography.
6. Run QA and preview after every meaningful revision.

When feedback is vague, propose 2-3 concrete remedies. For example, for "this page is empty", choose among: shrinking the card, adding evidence mini-cards, converting it to a full-image page, or rewriting the text as a denser result-to-conclusion paragraph.

## 7. Final Delivery

Before final response:
- Save final PPTX.
- Run structural QA.
- Render previews/contact sheet if possible.
- Run visual QA on rendered previews if available.
- Open or inspect key pages.
- Report output path and known caveats.
