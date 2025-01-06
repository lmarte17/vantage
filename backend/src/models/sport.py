from pydantic import BaseModel


class Sport(BaseModel):
    key: str
    group: str
    title: str
    active: bool
    has_outrights: bool