def calculate_score(

    semantic_score,
    experience_score,
    behavior_score

):

    final_score = (

        semantic_score * 0.6 +

        experience_score * 0.25 +

        behavior_score * 0.15
    )

    return round(final_score, 2)
