# myFirstMLApp

# myFirstMLApp — NLTK VADER Sentiment Analyzer (Python)

A minimal Python script that assigns a sentiment score and label (**Positive / Neutral / Negative**) to a list of input strings using **NLTK’s VADER** sentiment model (`SentimentIntensityAnalyzer`).

This repo is intentionally small: it is meant to be a clean starting point you can evolve into a reusable CLI tool, API, or batch processor.

---

## What it does

Given an array (list) of strings, the script prints for each string:

- the original text
- the **compound sentiment score** (range: `-1.0` to `1.0`)
- a label:
  - `Positive` if score `>= 0.05`
  - `Negative` if score `<= -0.05`
  - `Neutral` otherwise

VADER is best suited for short, social-style text (reviews, feedback, comments), and is a strong baseline for quick sentiment classification.

---

## Project structure

- `main.py` — script entry point (currently a single-file prototype)
- `pyproject.toml` / `poetry.lock` — dependency management (Poetry)
- `.replit` / `replit.nix` — Replit configuration (optional)

---

## Requirements

- Python 3.10+
- NLTK 3.8+

If you are running locally (not in Replit), you will also need the NLTK VADER lexicon downloaded.

---

## Setup

### Option A — Poetry (recommended for this repo)

```bash
poetry install
