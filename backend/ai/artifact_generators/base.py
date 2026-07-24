from sqlalchemy.orm import Session

from ai.context.builder import ContextBuilder
from ai.providers.ollama_provider import OllamaProvider


class BaseGenerator:

    def __init__(self, db: Session):

        self.db = db

        self.context_builder = ContextBuilder(db)

        self.llm = OllamaProvider()

    def generate(self, document_id: int):

        raise NotImplementedError