# Layout Rules

## Grid and Alignment

Use a fixed 16:9 grid:

```text
slide: 13.333 x 7.5 in
content x: 0.72
content width: 11.89
title bar height: ~0.64
footer y: ~7.12
conclusion y: ~6.18
```

Align by object frames:
- title frame
- image frame
- text/card frame
- conclusion bar
- footer line

Do not align by the visible edge of a cropped image.

## Cover and Thanks

Use a center-axis composition:

- school logo centered
- title centered
- subtitle centered
- report type centered
- author/supervisor centered
- date centered

The thanks page should use the same center-axis logic. Do not leave logo, title, and subtitle slightly offset.

## Content Page Patterns

### Full Image Page

Use for:
- technical route
- factor system
- architecture
- flow diagrams

Pattern:
- title bar
- large image frame
- one conclusion bar

If the figure is visually thin, add a short explanation bar above or below and crop/fill carefully.

### Image + Analysis Page

Use for:
- mechanism explanations
- static result
- robustness
- backtest

Preferred structure:

```text
image side: 55-60% width
text side:
  compact analysis card
  note/boundary card
  keyword strip
  evidence mini-cards
bottom:
  conclusion bar
```

This avoids large empty analysis boxes while preserving a clear reading path.

### Dual Image Page

Use for:
- rolling + multistep
- factor contribution + ablation

Pattern:
- two aligned captions
- two equal image frames
- result interpretation band
- conclusion bar

## Typography

Keep same-level text consistent:

| Role | Suggested Size |
|---|---:|
| title bar | 21 pt |
| subtitle | 9.5 pt |
| analysis body | 10.5-10.8 pt |
| note card | 10 pt |
| evidence mini-card title | 8.8 pt |
| evidence mini-card body | 7.5-7.8 pt |
| conclusion bar | 11.5-12 pt |
| footer | 8.5 pt |

Use one CJK font family consistently, such as Microsoft YaHei or the template's default Chinese font.

## Empty Space Rules

Empty space is useful only when it improves focus. It becomes a problem when:
- a large bordered card contains only a few lines
- one column ends far above the other column
- evidence pages have no local interpretation
- images are small but text cards are huge

Fixes:
- shrink the card instead of filling it with filler text
- add keyword strip
- add evidence mini-cards
- split content into two smaller cards
- increase image size or rebalance columns

## Color and Emphasis

- Use the template's main color for titles and borders.
- Use accent colors sparingly for sections.
- Use deep red bold for key metrics only.
- Avoid one-note palettes and excessive decorative gradients.

## Forbidden Patterns

- bullet-only pages
- tag-only analysis
- text/image overlap
- nested cards
- large empty bordered panels
- inconsistent font sizes for the same semantic role
- decorative elements that do not carry information
