import numpy as np
from sentence_transformers import SentenceTransformer

from ..aggregates.sentence_collection import SentenceCollection
from ..entities.sentence import Sentence
from ..value_objects.embedding import Embedding


class SemanticSearchService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.sentence_collection = SentenceCollection()

    def add_sentence(self, text: str):
        embedding_vector = self.model.encode([text])[0]
        embedding = Embedding(vector=embedding_vector)
        sentence = Sentence(text=text, embedding=embedding)
        self.sentence_collection.add_sentence(sentence)

    def find_intention(self, query: str) -> str:
        query_embedding_vector = self.model.encode([query])[0]
        query_embedding = Embedding(vector=query_embedding_vector)
        most_similar_sentence = self.sentence_collection.find_most_similar(
            query_embedding)
        return most_similar_sentence.text
