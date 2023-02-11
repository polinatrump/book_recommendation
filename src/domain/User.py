import pydantic


class User(pydantic.BaseModel):
    id: int
    first_name: str
    last_name: str

