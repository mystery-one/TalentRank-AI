# TalentRank AI

### Semantic Recruitment Intelligence System

An AI-powered recruitment ranking system that intelligently matches candidates to job descriptions using semantic understanding, vector embeddings, FAISS retrieval, and hybrid weighted scoring.

Unlike traditional ATS systems that rely only on keyword matching, TalentRank AI evaluates contextual relevance, transferable skills, profile quality, experience alignment, and semantic similarity to generate recruiter-trustworthy candidate rankings.

---

# Problem Statement

Traditional Applicant Tracking Systems (ATS) often fail to identify high-quality candidates because they rely heavily on exact keyword matching.

This leads to:

* Missing qualified candidates
* Poor contextual understanding
* Weak candidate-job alignment
* Increased recruiter screening time
* Low trust in automated shortlisting

TalentRank AI addresses these limitations using semantic search and explainable AI-driven candidate ranking.

---

# Key Features

* Semantic candidate retrieval using Sentence Transformers
* FAISS-based scalable vector similarity search
* Hybrid weighted candidate ranking
* Explainable AI ranking insights
* Candidate profile quality analysis
* Context-aware job description understanding
* Fast retrieval across large candidate datasets
* CSV and JSON ranking export support

---

# System Workflow

1. Job Description is provided as input
2. Candidate profiles are processed and cleaned
3. Semantic embeddings are generated
4. FAISS retrieves contextually relevant candidates
5. Multiple candidate signals are evaluated
6. Hybrid weighted scoring calculates final rankings
7. Explainability layer generates ranking insights
8. Ranked outputs are exported

---

# Hybrid Ranking Methodology

The final candidate score is generated using a hybrid weighted scoring approach:

```python
Final Score =
0.50 × Semantic Similarity +
0.30 × Experience Relevance +
0.20 × Profile Quality Score
```

### Signals Considered

* Semantic Similarity
* Experience Relevance
* Skills Alignment
* Project Relevance
* Profile Completeness
* Contextual Matching

---

# Explainability Layer

The system generates explainable ranking insights including:

* Match Scores
* Confidence Levels
* Candidate Strengths
* Ranking Reasons
* Skill Alignment Insights

This improves recruiter trust and transparency in candidate evaluation.

---

# Technologies Used

| Technology            | Purpose                       |
| --------------------- | ----------------------------- |
| Python                | Core backend development      |
| Sentence Transformers | Semantic embedding generation |
| FAISS                 | Vector similarity search      |
| Pandas                | Data processing               |
| NumPy                 | Numerical operations          |
| tqdm                  | Progress tracking             |
| python-docx           | Job description parsing       |

---

# Project Structure

```text
TalentRank-AI/
│
├── core/                   # Ranking and search modules
├── dataset/                # Candidate dataset (not uploaded)
├── outputs/                # Generated outputs and embeddings
├── utils/                  # Utility functions
├── app.py                  # Main execution file
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/mystery-one/TalentRank-AI.git
cd TalentRank-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Dataset Setup

Due to GitHub file size limitations, the dataset is not included in this repository.

Place the dataset file:

```text
candidates.jsonl
```

inside:

```text
dataset/
```

---

# Run Application

```bash
python app.py
```

---

# Output Files

Generated ranking outputs will automatically be saved inside:

```text
outputs/
```

Example generated files:

* final_rankings.csv
* final_rankings.json
* candidate_embeddings.npy

---

# Sample Ranking Output

| Rank | Candidate ID | Final Score | Semantic Score | Experience Score | Profile Quality Score |
| ---- | ------------ | ----------- | -------------- | ---------------- | --------------------- |
| 1    | CAND_0000112 | 76.50       | 98.49          | 50               | 32                    |
| 2    | CAND_0000723 | 76.50       | 98.44          | 50               | 32                    |
| 3    | CAND_0000343 | 76.15       | 98.45          | 50               | 30                    |

---

# Screenshots

## Candidate Ranking Output
<img width="1915" height="991" alt="ranking_output1 png" src="https://github.com/user-attachments/assets/cbfe99f3-842c-4d6e-960c-01fd534b08cb" />

<img width="1912" height="992" alt="ranking_output2 png" src="https://github.com/user-attachments/assets/660f9b54-4ea8-413c-90b0-c4c30dfeb5c4" />


---

## Terminal Execution



---

## System Architecture

<img width="1564" height="692" alt="architecture_diagram" src="https://github.com/user-attachments/assets/9f3377d8-b358-4303-a367-676f082c27a9" />


---

# Traditional ATS vs TalentRank AI

| Traditional ATS             | TalentRank AI                |
| --------------------------- | ---------------------------- |
| Keyword matching            | Semantic understanding       |
| Limited contextual analysis | Context-aware ranking        |
| Misses transferable skills  | Detects semantic relevance   |
| Static filtering            | Hybrid intelligent scoring   |
| Low explainability          | Explainable ranking insights |

---

# Challenges Addressed

* Eliminates dependency on exact keyword matching
* Detects transferable skills through semantic understanding
* Improves recruiter shortlist quality
* Reduces irrelevant candidate retrieval
* Handles large-scale candidate retrieval efficiently
* Generates explainable candidate rankings

---

# Future Improvements

* Recruiter feedback learning loop
* Adaptive ranking optimization
* Resume parsing automation
* LLM-powered candidate summaries
* Bias-aware ranking analysis
* Real-time recruiter dashboard

---

# Submission Assets

* GitHub Repository
* PPT / PDF Documentation
* Ranked Candidate Output File
* System Architecture Diagrams
* Demo Screenshots

---

# Important Notes

* Dataset files are excluded due to GitHub file size restrictions
* Generated outputs are ignored using `.gitignore`
* The system is designed for scalable semantic candidate retrieval

---

# License

This project is intended for educational and hackathon purposes.

---

# Author

Prakruthi D Koppad

AI / ML Engineer | Semantic Search | Recruitment Intelligence Systems
