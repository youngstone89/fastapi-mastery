# app/features/semantic_search/application/usecases/semantic_search_usecase.py
from app.features.semantic_search.domain.services.semantic_search_service import \
    SemanticSearchService


class SemanticSearchUseCase:
    def __init__(self, semantic_search_service: SemanticSearchService):
        self.service = semantic_search_service

    def add_sentence(self, text: str):
        self.service.add_sentence(text)

    async def find_intention(self, query: str) -> str:
        return await self.service.async_find_intention(query)
