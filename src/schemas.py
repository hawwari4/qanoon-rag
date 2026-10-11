"""Data contracts.

`Article` is the contract between path 1 (indexing) and path 2 (serving):
path 1 must produce records that pass this model, and path 2 relies on its fields
to cite articles and to flag repealed ones.
"""

from pydantic import BaseModel, ConfigDict, Field, computed_field


class Article(BaseModel):
    """One article of the Egyptian Civil Code."""

    model_config = ConfigDict(str_strip_whitespace=True)

    article_number: int = Field(gt=0)
    text_ar: str = Field(min_length=1)
    text_en: str = ""
    book: str | None = None
    chapter: str | None = None
    is_repealed: bool = False
    source_page: int | None = Field(default=None, gt=0)

    @computed_field
    @property
    def citation(self) -> str:
        return f"Egyptian Civil Code, Article {self.article_number}"


class AskRequest(BaseModel):
    """Body of POST /ask."""

    model_config = ConfigDict(str_strip_whitespace=True)

    question: str = Field(min_length=1, max_length=1000, examples=["ما هي أركان العقد؟"])


class AskResponse(BaseModel):
    """Answer with the articles it is based on."""

    answer: str
    sources: list[str]
    model: str
