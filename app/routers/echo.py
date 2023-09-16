from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EchoRequest(BaseModel):
    echo: str


@router.post("/", tags=["echo"])
async def echo(req: EchoRequest):
    return req.echo
