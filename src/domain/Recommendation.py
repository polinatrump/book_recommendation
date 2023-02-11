from typing import List

import pydantic


class Recommendation(pydantic.BaseModel):
    id: int
    # recommendations: List[str]
    book_id = int
    user_id = int

