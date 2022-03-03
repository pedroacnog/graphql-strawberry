from typing import Optional
from fastapi import FastAPI
from sqlmodel import (
  SQLModel,
  Field,
  create_engine,
  select,
  Session
)

# Criar engine do banco
engine = create_engine('sqlite:///database.db')

class Pessoa(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  nome: str
  idade: int

# Cria o banco de dados
SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.get('/')
def home():
  return {'message':'teste Ok'}

@app.get('/pessoa')
def get_pessoa():
  query = select(Pessoa)
  with Session(engine) as session:
    result = session.execute(query).scalars().all()
  return result