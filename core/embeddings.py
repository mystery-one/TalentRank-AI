from sentence_transformers import (
    SentenceTransformer
)

from config import MODEL_NAME

model = SentenceTransformer(
    MODEL_NAME
)

from sentence_transformers import ( 
    SentenceTransformer
)

from config import MODEL_NAME 
model = SentenceTransformer( 
    MODEL_NAME 
)

def generate_embedding(texts): 
    return model.encode( 
        texts,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True 
        )
