# AI Recruiter Ranking System

## Production-Style AI Hiring Assistant

An AI-powered recruiter intelligence system designed to help recruiters identify high-quality candidates using:

* Semantic Search
* Vector Embeddings
* Hybrid Scoring
* Explainable AI
* Contextual Candidate Ranking

This system goes beyond keyword matching and evaluates candidates holistically using skills, experience, projects, behavioral signals, and semantic relevance.

---

# Problem Statement

Traditional ATS (Applicant Tracking Systems):

* Rely heavily on keyword matching
* Miss transferable skills
* Ignore contextual relevance
* Cannot understand semantic meaning
* Produce low-trust rankings

Example:

A candidate with:

* Computer Vision
* PyTorch
* MLOps

may still be highly relevant for an AI Engineer role even without exact keyword overlap.

Traditional systems fail in such cases.

---

# Proposed Solution

This project builds a production-style AI recruiter system that:

✅ Understands job descriptions semantically
✅ Evaluates candidates holistically
✅ Uses vector embeddings + semantic search
✅ Applies hybrid weighted scoring
✅ Produces explainable recruiter-friendly rankings

---

# Key Features

* Semantic candidate matching
* Vector embeddings using SentenceTransformers
* FAISS similarity search
* Hybrid scoring engine
* Explainable AI ranking
* Recruiter-friendly outputs
* Modular scalable architecture
* Embedding caching
* Production-style folder structure

---

# Tech Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Language          | Python                |
| Embeddings        | Sentence Transformers |
| Vector Search     | FAISS                 |
| Data Processing   | Pandas                |
| ML Utilities      | NumPy                 |
| Progress Tracking | tqdm                  |
| Document Parsing  | python-docx           |

---

# System Architecture

```text
Job Description
        ↓
JD Semantic Parsing
        ↓
Embedding Generation
        ↓
FAISS Vector Search
        ↓
Top Semantic Matches
        ↓
Hybrid Scoring Engine
        ↓
Behavioral Evaluation
        ↓
Explainability Layer
        ↓
Final Ranked Candidates
```

---

# Project Structure

```text
ai-recruiter-ranking-system/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── core/
│   ├── embeddings.py
│   ├── ranking_engine.py
│   ├── semantic_search.py
│   ├── candidate_loader.py
│   ├── jd_parser.py
│   ├── hybrid_scoring.py
│   ├── explainability.py
│   └── behavioral_engine.py
│
├── dataset/
│   ├── job_description.docx
│   ├── sample_submission.csv
│   ├── validate_submission.py
│   └── redrob_signals_doc.docx
│
├── outputs/
│   └── .gitkeep
│
└── utils/
```

---

# Installation

## Step 1 — Clone Repository

```bash
git clone https://github.com/mystery-one/ai-recruiter-ranking-system.git
```

---

## Step 2 — Navigate to Project

```bash
cd ai-recruiter-ranking-system
```

---

## Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Run Main Pipeline

```bash
python app.py
```

---

# Expected Workflow

```text
Loading candidates...
Reading job description...
Generating embeddings...
Building FAISS index...
Running semantic retrieval...
Ranking candidates...
Generating explainability...
Saving outputs...
```

---

# Output Files

The system generates recruiter-friendly outputs:

```text
outputs/
│
├── final_rankings.csv
└── final_rankings.json
```

---

# Sample Output Format

| Rank | Candidate   | Final Score | Confidence |
| ---- | ----------- | ----------- | ---------- |
| 1    | Candidate A | 92.4        | High       |
| 2    | Candidate B | 89.7        | High       |
| 3    | Candidate C | 86.3        | Medium     |

---

# Hybrid Scoring Logic

Final candidate ranking is based on:

| Component            | Weight |
| -------------------- | ------ |
| Semantic Similarity  | 60%    |
| Experience Relevance | 25%    |
| Behavioral Score     | 15%    |

---

# Semantic Retrieval

The system uses:

* SentenceTransformer embeddings
* Dense vector representation
* FAISS nearest-neighbor retrieval

This allows semantic matching instead of exact keyword overlap.

---

# Explainability Layer

Each ranked candidate includes:

* Final Score
* Semantic Score
* Experience Score
* Behavioral Score
* Strengths
* Confidence Level
* Ranking Reasoning

Example:

```json
{
  "rank": 1,
  "final_score": 92.1,
  "confidence": "High",
  "strengths": [
    "Strong AI/ML alignment",
    "Relevant project experience",
    "High semantic similarity"
  ]
}
```

---

# Optimization Features

## Embedding Caching

Embeddings are cached locally to reduce repeated computation.

## Batch Embedding Generation

Embeddings are generated in batches for faster processing.

## Scalable Retrieval

FAISS enables fast vector similarity search for large candidate datasets.

---

# Evaluation Metrics

The system can be evaluated using:

* Precision@K
* Recall@K
* Recruiter Acceptance Rate
* Ranking Consistency
* Semantic Relevance Accuracy

---

# Screenshots

## Architecture Diagram

> Add architecture screenshot here

---

## Terminal Execution

> Add terminal execution screenshot here

---

## Ranked Output CSV

> Add ranked output screenshot here

---

## GitHub Repository

> Add GitHub repository screenshot here

---

# Current Limitations

* No true LLM reasoning yet
* Limited career trajectory analysis
* Limited project-depth understanding
* No recruiter dashboard yet
* No API deployment yet

---

# Future Improvements

* GPT/Claude-powered reranking
* Multi-role candidate matching
* Skill graph intelligence
* Recruiter dashboard
* Candidate clustering
* Interview question generation
* Bias mitigation layer
* Resume summarization
* API deployment with FastAPI

---

# Why This System Matters

This system improves:

✅ Recruiter efficiency
✅ Hiring quality
✅ Semantic candidate understanding
✅ Explainable AI hiring
✅ Faster candidate screening

---

# Business Impact

| Metric                     | Improvement           |
| -------------------------- | --------------------- |
| Resume Screening Time      | Reduced significantly |
| Candidate Quality          | Improved              |
| Recruiter Trust            | Increased             |
| Keyword Dependency         | Reduced               |
| Semantic Matching Accuracy | Improved              |

---

# Author

Prakruthi D Koppad

---

# License

This project is intended for educational and challenge submission purposes.
