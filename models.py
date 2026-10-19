
from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(100), nullable=False)
    concluida = Column(Boolean, default=False, nullable=False)
