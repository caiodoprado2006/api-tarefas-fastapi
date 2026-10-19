
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

import models
from database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Gerenciamento de Tarefas")


def obter_banco():
    banco = SessionLocal()
    try:
        yield banco
    finally:
        banco.close()


class TarefaCriacao(BaseModel):
    descricao: str = Field(min_length=3, max_length=100)


class TarefaAtualizacao(BaseModel):
    descricao: str = Field(min_length=3, max_length=100)



class TarefaResposta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    descricao: str
    concluida: bool


@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API está funcionando!"}


@app.get("/tarefas", response_model=list[TarefaResposta])
def listar_tarefas(banco: Session = Depends(obter_banco)):
    return banco.query(models.Tarefa).all()


@app.post("/tarefas", response_model=TarefaResposta)
def cadastrar_tarefa(
    dados: TarefaCriacao,
    banco: Session = Depends(obter_banco)
):
    tarefa = models.Tarefa(
        descricao=dados.descricao,
        concluida=False
    )

    banco.add(tarefa)
    banco.commit()
    banco.refresh(tarefa)

    return tarefa


@app.patch(
    "/tarefas/{tarefa_id}/concluir",
    response_model=TarefaResposta
)
def concluir_tarefa(
    tarefa_id: int,
    banco: Session = Depends(obter_banco)
):
    tarefa = banco.query(models.Tarefa).filter(
        models.Tarefa.id == tarefa_id
    ).first()

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    tarefa.concluida = True
    banco.commit()
    banco.refresh(tarefa)

    return tarefa


@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(
    tarefa_id: int,
    banco: Session = Depends(obter_banco)
):
    tarefa = banco.query(models.Tarefa).filter(
        models.Tarefa.id == tarefa_id
    ).first()

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    banco.delete(tarefa)
    banco.commit()

    return {
        "mensagem": "Tarefa excluída com sucesso",
        "tarefa": {
            "id": tarefa.id,
            "descricao": tarefa.descricao,
            "concluida": tarefa.concluida
        }
    }


@app.patch("/tarefas/{tarefa_id}")
def atualizar_tarefa(
    tarefa_id: int,
    dados: TarefaAtualizacao,
    banco: Session = Depends(obter_banco)
):
    tarefa = banco.query(models.Tarefa).filter(
        models.Tarefa.id == tarefa_id
    ).first()

    if tarefa is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    tarefa.descricao = dados.descricao
    banco.commit()
    banco.refresh(tarefa)

    return tarefa
