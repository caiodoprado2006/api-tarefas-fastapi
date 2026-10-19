
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel, Field

app = FastAPI(title="API de Gerenciamento de Tarefas")


class TarefaCriacao(BaseModel):
    descricao: str = Field(
        min_length=3,
        max_length=100,
        description="Descrição da tarefa, entre 3 e 100 caracteres"
    )


tarefas = []
proximo_id = 1


@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API está funcionando!"}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas")
def cadastrar_tarefa(dados: TarefaCriacao):
    global proximo_id

    tarefa = {
        "id": proximo_id,
        "descricao": dados.descricao,
        "concluida": False
    }

    tarefas.append(tarefa)
    proximo_id += 1

    return tarefa


@app.patch("/tarefas/{tarefa_id}/concluir")
def concluir_tarefa(tarefa_id: int):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            return tarefa

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            tarefa_removida = tarefas.pop(indice)
            return {
                "mensagem": "Tarefa excluída com sucesso",
                "tarefa": tarefa_removida
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )
