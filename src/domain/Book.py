from typing import List, Optional
import pydantic
from src.domain.Author import Author
from src.domain.Genre import Genre


class Book(pydantic.BaseModel):
    id: int
    authors: Optional[List[Author]]
    rating: float
    rating_count: int
    review_count: int
    title: str
    genres: Optional[List[Genre]]
    image_url: Optional[str]
    genres_bin: str
    authors_bin: str
