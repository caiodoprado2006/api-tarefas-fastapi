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