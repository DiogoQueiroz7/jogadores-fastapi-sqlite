from sqlalchemy import Column, Integer, String
from database import Base


class Jogador(Base):
    __tablename__ = "jogadores"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    posicao = Column(String)