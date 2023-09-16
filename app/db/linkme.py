from sqlmodel import SQLModel, Field


class Link(SQLModel, table=True):
    path: str = Field(primary_key=True)
    short_path: str
