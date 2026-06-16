
import json
import pandas as pd

def load_candidates(path):

    candidates = []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            candidates.append(
                json.loads(line)
            )

    return pd.DataFrame(
        candidates
    )
