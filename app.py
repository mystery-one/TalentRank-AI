import pandas as pd

from core.candidate_loader import (
    load_candidates
)

from core.jd_parser import (
    extract_jd_text
)

from core.ranking_engine import (
    RankingEngine
)

from config import TOP_K

print("\nLoading candidates...")

candidates = load_candidates(
    "dataset/candidates.jsonl"
)

# FAST VALIDATION MODE

candidates = candidates.head(1000)

print(
    f"Loaded {len(candidates)} candidates."
)

print("\nReading Job Description...")

jd_text = extract_jd_text(
    "dataset/job_description.docx"
)

print("\nBuilding ranking engine...")

engine = RankingEngine()

engine.prepare_candidates(
    candidates
)

print("\nRanking candidates...")

results = engine.rank_candidates(

    jd_text,

    candidates,

    TOP_K
)

results_df = pd.DataFrame(
    results
)

results_df.to_csv(

    "outputs/final_rankings.csv",

    index=False
)

results_df.to_json(

    "outputs/final_rankings.json",

    orient="records",

    indent=4
)

print(
    "\nSUCCESS: Rankings generated."
)

print(
    "\nFiles saved in outputs/"
)

