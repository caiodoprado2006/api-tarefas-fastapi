# API de Gerenciamento de Tarefas

API REST desenvolvida com Python e FastAPI para cadastrar, listar, atualizar, concluir e excluir tarefas. O projeto utiliza SQLite para persistência de dados e Pytest para testes automatizados.

Projeto de portfólio desenvolvido durante meus estudos de Engenharia de Software, com foco em Backend Python.

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Pytest
- Git e GitHub

## Funcionalidades

- Cadastro de tarefas com validação de dados
- Listagem de tarefas
- Atualização da descrição de uma tarefa
- Conclusão de tarefas
- Exclusão de tarefas
- Filtro por status: pendente ou concluída
- Paginação de resultados
- Persistência dos dados em SQLite
- Respostas de erro para tarefas inexistentes
- Testes automatizados dos endpoints

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verificar se a API está funcionando |
| GET | `/tarefas/` | Listar tarefas |
| POST | `/tarefas/` | Cadastrar tarefa |
| PATCH | `/tarefas/{tarefa_id}` | Atualizar descrição |
| PATCH | `/tarefas/{tarefa_id}/concluir` | Concluir tarefa |
| DELETE | `/tarefas/{tarefa_id}` | Excluir tarefa |

## Filtros e paginação

O endpoint `GET /tarefas/` aceita os seguintes parâmetros:

| Parâmetro | Descrição | Padrão |
|---|---|---|
| `concluida` | Filtra por status (`true` ou `false`) | Todos os status |
| `limite` | Quantidade de tarefas por página, de 1 a 100 | `10` |
| `pagina` | Número da página, a partir de 1 | `1` |

Exemplo de consulta:

```text
/tarefas/?concluida=false&limite=5&pagina=1
```

Essa consulta retorna até cinco tarefas pendentes da primeira página.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/caiodoprado2006/api-tarefas-fastapi.git
cd api-tarefas-fastapi
```

### 2. Criar e ativar o ambiente virtual

No Windows com PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
py -m pip install -r requirements.txt
```

### 4. Criar as tabelas do banco de dados

```powershell
py init_db.py
```

### 5. Iniciar a API

```powershell
py -m uvicorn main:app --reload
```

A documentação interativa estará disponível em:

http://127.0.0.1:8000/docs

## Executar os testes

Com o ambiente virtual ativado, execute:

```powershell
py -m pytest -v
```

Os testes verificam os principais endpoints, as validações, os filtros, a paginação e os erros esperados.

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

- `main.py`: inicializa a aplicação FastAPI.
- `routers/tarefas.py`: implementa os endpoints.
- `database.py`: configura o acesso ao banco de dados.
- `models.py`: define o modelo da tabela de tarefas.
- `init_db.py`: cria as tabelas do banco.
- `test_main.py`: contém os testes automatizados.

## Melhorias futuras

- Migrar de SQLite para PostgreSQL
- Adicionar autenticação de usuários
- Melhorar a organização dos testes
- Configurar integração contínua
- Disponibilizar a API em um serviço de hospedagem

## Autor

Caio do Prado

Estudante de Engenharia de Software, com foco em desenvolvimento Backend com Python.

GitHub: https://github.com/caiodoprado2006
