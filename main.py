
from fastapi import FastAPI

from database import Base, engine
from routers.tarefas import router as tarefas_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Gerenciamento de Tarefas")

app.include_router(tarefas_router)


@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API está funcionando!"}
