import os
import numpy as np
import pandas as pd

from tqdm import tqdm

from core.embeddings import (
    generate_embedding
)

from core.semantic_search import (
    SemanticSearchEngine
)

from core.hybrid_scoring import (
    calculate_score
)

from core.behavioral_engine import (
    get_behavior_score
)

from core.explainability import (
    generate_reasoning
)


class RankingEngine:

    def __init__(self):

        self.search_engine = (
            SemanticSearchEngine()
        )

        self.candidate_texts = []

        self.embeddings = None

    def build_candidate_text(
        self,
        row
    ):

        skills = str(
            row.get("skills", "")
        )

        experience = str(
            row.get("experience", "")
        )

        projects = str(
            row.get("projects", "")
        )

        summary = str(
            row.get("summary", "")
        )

        education = str(
            row.get("education", "")
        )

        combined_text = f"""

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Summary:
{summary}

Education:
{education}
"""

        return combined_text

    def prepare_candidates(
        self,
        candidates_df
    ):

        print(
            "\nPreparing candidate text..."
        )

        self.candidate_texts = []

        for _, row in tqdm(

            candidates_df.iterrows(),

            total=len(candidates_df),

            desc="Processing Candidates"
        ):

            combined_text = (
                self.build_candidate_text(
                    row
                )
            )

            self.candidate_texts.append(
                combined_text
            )

        cache_path = (
            "outputs/candidate_embeddings.npy"
        )

        if os.path.exists(cache_path):

            print(
                "\nLoading cached embeddings..."
            )

            embeddings = np.load(
                cache_path
            )

        else:

            print(
                "\nGenerating embeddings..."
            )

            embeddings = generate_embedding(
                self.candidate_texts
            )

            np.save(
                cache_path,
                embeddings
            )

            print(
                "\nEmbeddings cached successfully."
            )

        self.embeddings = embeddings

        self.search_engine.build_index(
            embeddings
        )

    def calculate_semantic_score(
        self,
        distance
    ):

        semantic_score = max(
            0,
            100 - float(distance)
        )

        return round(
            semantic_score,
            2
        )

    def calculate_experience_score(
        self,
        candidate
    ):

        experience_fields = [

            "years_experience",

            "experience_years",

            "experience"
        ]

        for field in experience_fields:

            value = candidate.get(
                field,
                None
            )

            if isinstance(
                value,
                (int, float)
            ):

                return min(
                    value * 10,
                    100
                )

        return 50

    def rank_candidates(

        self,

        jd_text,

        candidates_df,

        top_k=100

    ):

        print(
            "\nGenerating JD embedding..."
        )

        jd_embedding = generate_embedding(
            [jd_text]
        )[0]

        print(
            "\nRunning semantic search..."
        )

        distances, indices = (
            self.search_engine.search(

                jd_embedding,

                top_k
            )
        )

        ranked_results = []

        print(
            "\nRanking candidates..."
        )

        for rank, idx in tqdm(

            enumerate(indices[0]),

            total=len(indices[0]),

            desc="Scoring Candidates"
        ):

            candidate = candidates_df.iloc[
                idx
            ]

            semantic_score = (
                self.calculate_semantic_score(
                    distances[0][rank]
                )
            )

            experience_score = (
                self.calculate_experience_score(
                    candidate
                )
            )

            behavior_score = (
                get_behavior_score(
                    candidate
                )
            )

            final_score = (
                calculate_score(

                    semantic_score,

                    experience_score,

                    behavior_score
                )
            )

            explanation = (
                generate_reasoning(

                    candidate,

                    final_score
                )
            )

            ranked_results.append({

                "rank":
                rank + 1,

                "candidate_id":
                candidate.get(
                    "candidate_id",
                    idx
                ),

                "final_score":
                final_score,

                "semantic_score":
                semantic_score,

                "experience_score":
                experience_score,

                "behavior_score":
                behavior_score,

                "confidence":
                explanation[
                    "confidence"
                ],

                "strengths":
                explanation[
                    "strengths"
                ],

                "reasoning":
                explanation[
                    "reasoning"
                ]
            })

        results_df = pd.DataFrame(
            ranked_results
        )

        results_df = results_df.sort_values(

            by="final_score",

            ascending=False
        )

        results_df.reset_index(

            drop=True,

            inplace=True
        )

        results_df["rank"] = (
            results_df.index + 1
        )

        return results_df