from sqlmodel import SQLModel, Field, MetaData


class Link(SQLModel, table=True):
    __tablename__ = "links"
    metadata = MetaData(schema="data")
    path: str = Field(primary_key=True)
    short_path: str
