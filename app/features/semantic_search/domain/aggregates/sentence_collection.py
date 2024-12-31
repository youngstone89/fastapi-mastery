
from typing import List

import numpy as np
from app.features.semantic_search.domain.entities.sentence import Sentence
from app.features.semantic_search.domain.value_objects.embedding import \
    Embedding


class SentenceCollection:
    def __init__(self):
        self._sentences: List[Sentence] = []

    def add_sentence(self, sentence: Sentence):
        self._sentences.append(sentence)

    def get_sentences(self) -> List[Sentence]:
        return self._sentences

    def find_most_similar(self, query_embedding: Embedding) -> Sentence:
        if not self._sentences:
            raise ValueError("No sentences in the collection")

        max_similarity = float('-inf')
        most_similar_sentence = None

        for sentence in self._sentences:
            if sentence.embedding is None:
                continue
            similarity = np.dot(query_embedding.vector,
                                sentence.embedding.vector)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_sentence = sentence

        if most_similar_sentence is None:
            raise ValueError("No sentence with embedding found")

        return most_similar_sentence

    async def async_find_most_similar(self, query_embedding: Embedding) -> Sentence:
        if not self._sentences:
            raise ValueError("No sentences in the collection")

        max_similarity = float('-inf')
        most_similar_sentence = None

        for sentence in self._sentences:
            if sentence.embedding is None:
                continue
            similarity = np.dot(query_embedding.vector,
                                sentence.embedding.vector)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_sentence = sentence

        if most_similar_sentence is None:
            raise ValueError("No sentence with embedding found")

        return most_similar_sentence
