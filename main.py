# # 오늘의 테이블
from fastapi import FastAPI
from routers import otas, webs, replys
import uvicorn

app = FastAPI()

app.include_router(webs.router)
app.include_router(otas.router, prefix='/otas')
app.include_router(replys.router, prefix='/replys')

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)