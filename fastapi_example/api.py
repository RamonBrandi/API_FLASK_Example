from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feichas(BaseModel):
    canal: str
    msg: str


@app.get("/", response_model=LinuxTips)
async def feichas():
    return feichas(
        canal="FEICHAS",
        msg="VAIIIIII",
    )