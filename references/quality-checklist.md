# Quality Checklist

## Content

- [ ] The thesis research topic is accurately understood.
- [ ] A page-level outline has been drafted from the thesis logic and confirmed when the task is not fully autonomous.
- [ ] Data sources are introduced.
- [ ] Research objects and selection logic are introduced.
- [ ] The proposed method is explained as a response to task difficulty.
- [ ] Core model design and innovation receive sufficient emphasis.
- [ ] Experiments form an evidence chain, not a chart dump.
- [ ] Every result slide states what conclusion the result supports.
- [ ] Backtest/application slides include boundary notes and do not overclaim.
- [ ] Summary states contributions, limitations, and future work.

## Visual Design

- [ ] Template style has been analyzed or manually summarized before generation.
- [ ] Cover is center-aligned.
- [ ] Thanks page is center-aligned.
- [ ] Agenda page is visually balanced.
- [ ] All title bars have consistent title/subtitle placement.
- [ ] Content uses a fixed grid.
- [ ] Image frames align with text/card frames.
- [ ] Conclusion bars align across pages.
- [ ] No page has a large empty analysis card.
- [ ] Text-heavy pages use cards/timelines/icons/evidence mini-cards.
- [ ] Figure-heavy pages include compact interpretation text.

## Typography

- [ ] Same semantic role uses same or near-same font size.
- [ ] Footer font is consistent.
- [ ] Analysis body font is consistent.
- [ ] Note card font is consistent.
- [ ] Conclusion bar font is consistent.
- [ ] No text is too small to read during defense.

## Figures

- [ ] Thesis figures are reused when appropriate.
- [ ] Generated figures are only used for missing conceptual/process diagrams.
- [ ] Generated figures use exact required text and are checked for text errors.
- [ ] Thin/long figures are cropped, re-laid out, or paired with explanation bars.
- [ ] Image aspect ratio is preserved unless intentional fill-cropping is used.

## Automated QA

Run:

```bash
python3 scripts/analyze_template.py template.pptx --json-out tmp/template_style.json
python3 scripts/pptx_qa.py deck.pptx --expected-slides 22 --warn-only
python3 scripts/render_contact_sheet.py deck.pptx --out-dir tmp/ppt_preview
python3 scripts/visual_qa.py tmp/ppt_preview/previews --warn-only
```

Check:
- [ ] slide count
- [ ] slide size
- [ ] out-of-bounds objects
- [ ] tiny text boxes
- [ ] bullet glyphs
- [ ] rough text-picture overlaps
- [ ] sparse large text boxes
- [ ] cover/thanks center-axis warnings
- [ ] weak alignment pages
- [ ] font size distribution
- [ ] preview contact sheet
- [ ] visual QA warnings judged or fixed

## Manual Preview

Inspect at least:
- [ ] cover
- [ ] agenda
- [ ] data page
- [ ] method gap page
- [ ] model architecture page
- [ ] key mechanism page
- [ ] static result page
- [ ] rolling/multistep page
- [ ] ablation/contribution page
- [ ] robustness page
- [ ] backtest page
- [ ] summary
- [ ] thanks
