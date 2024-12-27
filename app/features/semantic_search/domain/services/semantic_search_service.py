
import asyncio
import threading
import time
from concurrent.futures import ProcessPoolExecutor
from functools import cache, partial
from multiprocessing import Pool, cpu_count

import numpy as np
from aiocache import cached
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
        print('[{}] add_sentence for {}'.format(
            current_thread, text))
        start = time.time()
        embedding_vector = self.model.encode(texts)[0]
        print('[{}] took {} for add_sentence for {} '.format(
            current_thread, time.time() - start, text))
        embedding = Embedding(vector=embedding_vector)
        sentence = Sentence(text=text, embedding=embedding)
        self.sentence_collection.add_sentence(sentence)

    def sync_find_intention(self, query: str) -> str:
        current_thread = threading.current_thread().native_id
        print('[{}] find_intention for {}'.format(
            current_thread, query))
        querys = [query * 100 for _ in range(10)]
        start = time.time()
        query_embedding_vector = self.model.encode(querys)[0]
        print('[{}] took {:.2f} seconds for find intention for {} '.format(
            current_thread, time.time() - start, query))
        query_embedding = Embedding(vector=query_embedding_vector)
        most_similar_sentence = self.sentence_collection.find_most_similar(
            query_embedding)
        return most_similar_sentence.text

    @cached(ttl=60)
    async def async_find_intention(self, query: str) -> str:
        current_thread = threading.current_thread().native_id
        print('[{}] find_intention for {}'.format(
            current_thread, query))
        querys = [query * 100 for _ in range(10)]
        start = time.time()
        embeddings = await asyncio.to_thread(
            self.model.encode, querys)
        query_embedding_vector = embeddings[0]
        print('[{}] took {:.2f} seconds for find intention for {} '.format(
            current_thread, time.time() - start, query))
        query_embedding = Embedding(vector=query_embedding_vector)
        most_similar_sentence = self.sentence_collection.find_most_similar(
            query_embedding)
        return most_similar_sentence.text

    async def async_find_intention_parallel(self, query: str) -> str:
        current_thread = threading.current_thread().native_id
        print('[{}] find_intention for {}'.format(
            current_thread, query))
        queries = [query * 100 for _ in range(10)]
        # Split queries into batches
        batch_size = 1
        batches = [queries[i:i + batch_size]
                   for i in range(0, len(queries), batch_size)]
        # Use multiprocessing Pool to encode batches
        loop = asyncio.get_running_loop()
        start = time.time()
        with ProcessPoolExecutor() as executor:
            encode_func = partial(self.model.encode)
            tasks = [loop.run_in_executor(
                executor, encode_func, batch) for batch in batches]
            results = await asyncio.gather(*tasks)

        # Flatten the results (since each batch returns a list of embeddings)
        embeddings = [embedding for batch in results for embedding in batch]
        query_embedding_vector = embeddings[0]
        print('[{}] took {:.2f} seconds for find intention for {} '.format(
            current_thread, time.time() - start, query))
        query_embedding = Embedding(vector=query_embedding_vector)
        most_similar_sentence = self.sentence_collection.find_most_similar(
            query_embedding)
        return most_similar_sentence.text
