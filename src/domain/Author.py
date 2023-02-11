import pydantic


class Author(pydantic.BaseModel):
    id: int
    name: str
