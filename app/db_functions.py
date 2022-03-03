from sqlmodel import Session, select
from models import Pessoa, Livro, engine

def create_pessoas(idade: int, nome: str):
  person = Pessoa(nome=nome, idade=idade)

  with Session(engine) as session:
    session.add(person)
    session.commit()
    session.refresh(person)
  return person

def get_pessoas():
  query = select(Pessoa)
  with Session(engine) as session:
    result = session.execute(query).scalars().all()
  return result


def get_livros():
  query = select(Livro)
  with Session(engine) as session:
    result = session.execute(query).scalars().all()
  return result

def create_livros(idade: int, nome: str):
  person = Pessoa(nome=nome, idade=idade)

  with Session(engine) as session:
    session.add(person)
    session.commit()
    session.refresh(person)
  return person
