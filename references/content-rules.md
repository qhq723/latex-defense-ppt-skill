# Content Rules

## Narrative Principles

- The PPT should follow the thesis logic, not a generic slide template.
- Defense slides are not a compressed thesis. They are a 10-minute evidence story.
- Every major experiment page must answer: what result was observed, and what conclusion does it prove?
- Do not invent claims. If the thesis does not provide a number, either omit it or mark it as approximate.

## Required Content Checks

Include when relevant:
- data sources and processing rules
- research targets and why they are heterogeneous
- feature/factor construction
- model design motivation
- model module functions
- baselines and metrics
- static prediction result
- dynamic/rolling result
- multistep result
- factor contribution
- ablation
- extreme-market robustness
- backtest or application validation
- limitations and future work

## Data Page

A good data page should answer:

- Where did data come from?
- What frequency and time range?
- How were mixed frequencies aligned?
- What target objects were chosen?
- Why do these objects represent heterogeneous scenarios?

Example structure:

| Area | Content |
|---|---|
| Source | public datasets, domain databases, crawled indicators, experimental records |
| Frequency | original sampling frequency; low-frequency variables aligned to the modeling calendar |
| Targets | Target A, Target B, Target C, Target D |
| Why | different categories, mechanisms, scenarios, or difficulty levels |

## Method Gap Page

Avoid saying the proposed model has "main shortcomings". Use:

| Task Difficulty | Existing Limitation | Proposed Response |
|---|---|---|
| single-series information insufficient | statistical models depend on price history | multi-source factor system |
| heterogeneous factors mixed | direct concatenation weakens economic meaning | grouped factor embedding |
| stage drivers switch | fixed weights miss regime changes | factor-fusion attention |
| long dependency and seasonality | RNNs struggle with long horizon and time context | temporal context + Transformer |

## Experiment Wording

Bad:

```text
精度提升 / DA领先 / 跨品种稳定
```

Better:

```text
本文模型在多类研究对象上取得更低误差，并保持更稳定的方向或类别判断能力。
这说明结构化特征融合不仅改善数值拟合，也增强了模型对关键变化趋势的识别能力。
```

## Highlighting

Use deep red bold only for:
- best metrics
- key percentages
- central conclusion words
- important risk caveats

Do not highlight too many words. A slide usually needs 2-6 highlighted fragments.

## Page Text Density

Avoid two extremes:
- full slide of dense paragraphs
- huge cards with two short lines and empty space

Preferred information unit:
- compact analysis card
- note/boundary card
- keyword strip
- evidence mini-cards
- conclusion bar

This gives the viewer multiple reading depths.
