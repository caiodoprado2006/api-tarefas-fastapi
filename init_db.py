
from database import Base, engine
from models import Tarefa

Base.metadata.create_all(bind=engine)

print("Tabela de tarefas criada com sucesso!")
