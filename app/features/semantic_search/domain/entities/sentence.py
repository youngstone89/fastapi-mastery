# app/features/semantic_search/domain/entities/sentence.py
from dataclasses import dataclass

from app.features.semantic_search.domain.value_objects.embedding import \
    Embedding


@dataclass
class Sentence:
    text: str
    embedding: Embedding | None = None

    def set_embedding(self, embedding: Embedding):
        self.embedding = embedding
