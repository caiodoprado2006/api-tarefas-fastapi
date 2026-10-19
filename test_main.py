
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from main import app
from routers.tarefas import obter_banco

# Banco SQLite temporário, isolado dos dados reais
engine_teste = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessaoTeste = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_teste,
)


def obter_banco_teste():
    banco = SessaoTeste()
    try:
        yield banco
    finally:
        banco.close()


app.dependency_overrides[obter_banco] = obter_banco_teste
client = TestClient(app)


@pytest.fixture(autouse=True)
def preparar_banco():
    Base.metadata.create_all(bind=engine_teste)
    yield
    Base.metadata.drop_all(bind=engine_teste)


def test_inicio():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == (
        "Minha primeira API está funcionando!"
    )


def test_cadastrar_tarefa():
    resposta = client.post(
        "/tarefas",
        json={"descricao": "Estudar Python"},
    )

    assert resposta.status_code == 200
    assert resposta.json()["descricao"] == "Estudar Python"
    assert resposta.json()["concluida"] is False


def test_rejeitar_descricao_curta():
    resposta = client.post(
        "/tarefas",
        json={"descricao": "Oi"},
    )

    assert resposta.status_code == 422


def test_listar_tarefas():
    client.post(
        "/tarefas",
        json={"descricao": "Estudar FastAPI"},
    )

    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
    assert len(resposta.json()) == 1


def test_concluir_tarefa():
    cadastro = client.post(
        "/tarefas",
        json={"descricao": "Estudar testes"},
    )
    tarefa_id = cadastro.json()["id"]

    resposta = client.patch(
        f"/tarefas/{tarefa_id}/concluir"
    )

    assert resposta.status_code == 200
    assert resposta.json()["concluida"] is True


def test_concluir_tarefa_inexistente():
    resposta = client.patch("/tarefas/999/concluir")
    assert resposta.status_code == 404


def test_excluir_tarefa():
    cadastro = client.post(
        "/tarefas",
        json={"descricao": "Excluir esta tarefa"},
    )
    tarefa_id = cadastro.json()["id"]

    resposta = client.delete(f"/tarefas/{tarefa_id}")

    assert resposta.status_code == 200
    assert len(client.get("/tarefas").json()) == 0


def test_excluir_tarefa_inexistente():
    resposta = client.delete("/tarefas/999")
    assert resposta.status_code == 404


def test_cadastrar_tarefa_com_descricao_vazia():
    resposta = client.post(
        "/tarefas",
        json={"descricao": ""},
    )

    assert resposta.status_code == 422


def test_cadastrar_tarefa_com_descricao_muito_longa():
    resposta = client.post(
        "/tarefas",
        json={"descricao": "A" * 101},
    )

    assert resposta.status_code == 422


def test_atualizar_tarefa():
    cadastro = client.post(
        "/tarefas",
        json={"descricao": "Estudar Python"}
    )
    tarefa_id = cadastro.json()["id"]

    resposta = client.patch(
        f"/tarefas/{tarefa_id}",
        json={"descricao": "Estudar FastAPI"}
    )

    assert resposta.status_code == 200
    assert resposta.json()["descricao"] == "Estudar FastAPI"


def test_atualizar_tarefa_inexistente():
    resposta = client.patch(
        "/tarefas/999",
        json={"descricao": "Estudar FastAPI"}
    )

    assert resposta.status_code == 404
