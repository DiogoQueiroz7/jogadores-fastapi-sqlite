from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import get_db
from tabelas import Jogador

class JogadorEntrada(BaseModel):
    nome: str
    posicao: str
class JogadorSaida(JogadorEntrada):
    id: int

    model_config = ConfigDict(from_attributes=True)

app = FastAPI()

@app.get("/jogadores/")
def listar_jogadores(posicao: str | None = None, banco: Session = Depends(get_db)) -> list[JogadorSaida]:
    consulta = banco.query(Jogador)
    if posicao is None:
        return consulta.all()
    return consulta.filter(func.lower(Jogador.posicao) == posicao.lower()).all()

@app.get("/jogadores/{jogador_id}")
def ver_jogador(jogador_id: int, banco: Session = Depends(get_db)) -> JogadorSaida | None:
    j = banco.get(Jogador, jogador_id)
    if j is not None:
        return j
    return None

@app.post("/jogadores/")
def criar_jogador(jogador: JogadorEntrada, banco: Session = Depends(get_db)) -> JogadorSaida:
    novo = Jogador(nome=jogador.nome, posicao=jogador.posicao.lower())
    banco.add(novo)
    banco.commit()
    banco.refresh(novo)
    return novo

@app.put("/jogadores/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: JogadorEntrada, banco: Session = Depends(get_db)) -> JogadorSaida | None:
    j = banco.get(Jogador, jogador_id)
    if j is not None:
        j.nome = jogador.nome
        j.posicao = jogador.posicao.lower()
        banco.commit()
        banco.refresh(j)
        return j
    return None

@app.delete("/jogadores/{jogador_id}")
def remover_jogador(jogador_id: int, banco: Session = Depends(get_db)) -> JogadorSaida | None:
    j = banco.get(Jogador, jogador_id)
    if j is not None:
        banco.delete(j)
        banco.commit()
        return j
    return None