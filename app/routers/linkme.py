import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select

from ..db.engine import get_db_engine
from ..db.linkme import Link

router = APIRouter()


class ShortenRequest(BaseModel):
    path: str


class ShortenResponse(BaseModel):
    short_id: str


class UnshortenResponse(BaseModel):
    path: str


@router.post("/", tags=["linkme"])
async def create_link(req: ShortenRequest, db=Depends(get_db_engine)):
    if db is None:
        raise Exception("Unable to connect to DB")

    link = req.path.lower()

    # Check if link exists
    with Session(db) as session:
        select_statement = select(Link).where(Link.path == link)
        select_results = session.exec(select_statement)
        shortened_link = select_results.one_or_none()

        # Create if not
        if shortened_link is None:
            shortened_link = Link(path=link, short_path=str(uuid.uuid4()))
            session.add(shortened_link)
            session.commit()

        # Return shortened value
        return ShortenResponse(short_id=shortened_link.short_path)


@router.get("/{short_link_id}", tags=["linkme"])
async def get_link(short_link_id: str, db=Depends(get_db_engine)):
    if db is None:
        raise Exception("Unable to connect to DB")

    # Check if link exists
    with Session(db) as session:
        select_statement = select(Link).where(Link.short_path == short_link_id)
        select_results = session.exec(select_statement)
        shortened_link = select_results.one_or_none()

        # Create if not
        if shortened_link is None:
            raise HTTPException(status_code=404, detail="Link not found")

        # Return shortened value
        return UnshortenResponse(path=shortened_link.path)
