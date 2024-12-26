
import threading
import time

import numpy as np
from sentence_transformers import SentenceTransformer

from ..aggregates.sentence_collection import SentenceCollection
from ..entities.sentence import Sentence
from ..value_objects.embedding import Embedding


class SemanticSearchService:
    def __init__(self):
        self.model = SentenceTransformer('all-mpnet-base-v2')
        self.sentence_collection = SentenceCollection()

    def add_sentence(self, text: str):
        texts = [text * 10 for _ in range(10)]
        current_thread = threading.current_thread().native_id
        print('{} add_sentence for {}'.format(
            current_thread, text))
        start = time.time()
        embedding_vector = self.model.encode(texts)[0]
        print('{} took {} for add_sentence for {} '.format(
            current_thread, time.time() - start, text))
        embedding = Embedding(vector=embedding_vector)
        sentence = Sentence(text=text, embedding=embedding)
        self.sentence_collection.add_sentence(sentence)

    def find_intention(self, query: str) -> str:
        current_thread = threading.current_thread().native_id
        print('{} find_intention for {}'.format(
            current_thread, query))
        querys = [query * 100 for _ in range(10)]
        start = time.time()
        query_embedding_vector = self.model.encode(querys)[0]
        print('{} took {} for find intention for {} '.format(
            current_thread, time.time() - start, query))
        query_embedding = Embedding(vector=query_embedding_vector)
        most_similar_sentence = self.sentence_collection.find_most_similar(
            query_embedding)
        return most_similar_sentence.text
