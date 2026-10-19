# API de Gerenciamento de Tarefas

API REST desenvolvida em Python com FastAPI para gerenciar tarefas.

## Tecnologias

- Python
- FastAPI
- Pydantic
- Pytest
- Git e GitHub

## Funcionalidades

- Cadastrar tarefas com validação de dados
- Listar tarefas
- Concluir tarefas pelo ID
- Excluir tarefas pelo ID
- Retornar erros HTTP para tarefas inexistentes
- Executar testes automatizados

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/caiodoprado2006/api-tarefas-fastapi.git
cd api-tarefas-fastapi
```

### 2. Criar e ativar o ambiente virtual

No Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
py -m pip install -r requirements.txt
```

### 4. Iniciar a API

```powershell
py -m uvicorn main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

A documentação interativa estará disponível em http://127.0.0.1:8000/docs.

## Executar os testes

```powershell
py -m pytest -v
```

## Armazenamento

Atualmente, as tarefas ficam armazenadas em memória e são perdidas quando o servidor é reiniciado.

## Autor

Caio — Estudante de Engenharia de Software, com foco em desenvolvimento backend com Python.


## Estrutura do projeto

```text
api-tarefas-fastapi/
├── routers/
│   ├── __init__.py
│   └── tarefas.py
├── main.py
├── database.py
├── models.py
├── init_db.py
├── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Arquitetura

- `main.py`: inicializa a aplicação FastAPI.
- `routers/tarefas.py`: contém os endpoints de gerenciamento de tarefas.
- `database.py`: configura a conexão e as sessões do banco SQLite.
- `models.py`: define o modelo da tabela de tarefas.
- `init_db.py`: permite criar as tabelas do banco.
- `test_main.py`: contém os testes automatizados com pytest.


## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verificar se a API está funcionando |
| GET | `/tarefas/` | Listar todas as tarefas |
| POST | `/tarefas/` | Cadastrar uma nova tarefa |
| PATCH | `/tarefas/{tarefa_id}` | Atualizar a descrição de uma tarefa |
| PATCH | `/tarefas/{tarefa_id}/concluir` | Marcar uma tarefa como concluída |
| DELETE | `/tarefas/{tarefa_id}` | Excluir uma tarefa |
