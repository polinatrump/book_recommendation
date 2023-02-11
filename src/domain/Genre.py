import pydantic


class Genre(pydantic.BaseModel):
    id: int
    name: str
