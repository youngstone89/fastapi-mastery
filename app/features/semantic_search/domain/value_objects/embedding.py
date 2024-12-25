# app/features/semantic_search/domain/value_objects/embedding.py
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Embedding:
    vector: np.ndarray

    def __post_init__(self):
        if not isinstance(self.vector, np.ndarray):
            raise ValueError("Embedding vector must be a numpy array")
        if self.vector.ndim != 1:
            raise ValueError("Embedding vector must be 1-dimensional")
