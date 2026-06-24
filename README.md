# TalentRank AI

### Semantic Recruitment Intelligence System

AI-powered semantic candidate ranking system designed to improve recruiter decision-making beyond traditional keyword-based ATS filtering.

TalentRank AI intelligently matches candidates to job descriptions using semantic understanding, vector embeddings, FAISS retrieval, explainable AI, and hybrid weighted scoring.

Unlike traditional ATS systems that rely only on exact keyword matching, TalentRank AI evaluates:

* contextual relevance
* transferable skills
* profile quality
* experience alignment
* semantic similarity

to generate recruiter-trustworthy candidate rankings.

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
* Transferable skill detection
* Scalable retrieval across large candidate datasets
* CSV and JSON ranking export support

---

# Why Semantic Search Matters

Traditional ATS systems often reject strong candidates when exact keywords are missing.

TalentRank AI uses semantic understanding to identify:

* transferable skills
* contextual relevance
* role similarity
* meaningful candidate-job alignment

even when wording differs between resumes and job descriptions.

This enables smarter and more recruiter-aligned candidate shortlisting.

---

# System Workflow

1. Job Description is provided as input
2. Candidate profiles are cleaned and processed
3. Semantic embeddings are generated
4. FAISS retrieves contextually relevant candidates
5. Multiple candidate signals are evaluated
6. Hybrid weighted scoring calculates final rankings
7. Explainability layer generates ranking insights
8. Ranked outputs are exported

---

# Hybrid Ranking Methodology

The final candidate score is generated using a hybrid weighted scoring approach:

```text
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

# System Architecture

The system architecture combines:

* semantic embedding generation
* FAISS-based vector retrieval
* hybrid weighted scoring
* explainability modules

to create an end-to-end AI recruitment intelligence pipeline.

## Architecture Diagram

![System Architecture](assets/architecture_diagram.png)

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
├── core/                         # Ranking and semantic search modules
├── dataset/                      # Candidate dataset (not uploaded)
├── outputs/                      # Generated outputs and embeddings
├── utils/                        # Utility functions
├── assets/                       # Screenshots and architecture diagrams
│
├── app.py                        # Main execution file
├── requirements.txt
├── README.md
├── .gitignore
└── candidate_profiles_sample.json
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

Generated ranking outputs are automatically stored inside:

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

![Ranking Output](assets/ranking_output1.png)

---

## Additional Ranking Results

![Additional Ranking Output](assets/ranking_output2.png)

---

## Terminal Execution

![Terminal Execution](assets/terminal_execution.png)

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
* Handles scalable candidate retrieval efficiently
* Generates explainable candidate rankings

---

# Future Improvements

* Recruiter feedback learning loop
* Adaptive ranking optimization
* Resume parsing automation
* LLM-powered candidate summaries
* Bias-aware ranking analysis
* Interactive recruiter analytics interface

---

# Submission Assets

* GitHub Repository
* PPT / PDF Documentation
* Ranked Candidate Output File
* System Architecture Diagram
* Demo Screenshots

---

# Important Notes

* Dataset files are excluded due to GitHub file size restrictions
* Generated outputs are ignored using `.gitignore`
* The system is designed for scalable semantic candidate retrieval
* This project is developed as a hackathon prototype for AI-powered recruitment intelligence

---

# License

This project is intended for educational and hackathon purposes.

---

# Author

## Prakruthi D Koppad

AI / ML Engineer
Semantic Search | Recruitment Intelligence Systems
