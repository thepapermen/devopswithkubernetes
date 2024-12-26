import ninja
from datetime import datetime


class TodoIn(ninja.Schema):
    txt: str


class TodoOut(ninja.Schema):
    id: int
    txt: str
    created_at: datetime = None
