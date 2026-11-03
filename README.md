# jogadores-fastapi-sqlite

Atividade da matéria do professor Rogério, onde fiz uma API usando FastAPI para cadastrar jogadores do Palmeiras.

Os jogadores ficam salvos no SQLite usando SQLAlchemy. O Alembic cria as tabelas do banco.

## Integrantes

- Diogo Queiroz

## Como rodar

Precisa ter Python instalado.

Abra o terminal na pasta onde quer baixar o projeto e execute os passos:

1. Clonar: git clone https://github.com/DiogoQueiroz7/jogadores-fastapi-sqlite.git

2. Entrar na pasta: cd jogadores-fastapi-sqlite

3. Criar o ambiente virtual: python -m venv .venv

4. Ativar no Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
   - Linux/Mac: `source .venv/bin/activate`

5. Instalar as dependências: python -m pip install -r requirements.txt

6. Criar as tabelas: alembic upgrade head

7. Rodar a API: fastapi dev main.py

Acesse http://127.0.0.1:8000/docs para testar pelo Swagger.

O banco começa vazio. O arquivo jogadores.db fica fora do GitHub, mas a pasta do Alembic está no repositório.

## Rotas

- GET /jogadores/ - Lista os jogadores.
- GET /jogadores/{jogador_id} - Busca pelo ID.
- POST /jogadores/ - Cadastra um jogador.
- PUT /jogadores/{jogador_id} - Edita um jogador.
- DELETE /jogadores/{jogador_id} - Exclui um jogador.

Também dá pra filtrar pela posição: /jogadores/?posicao=goleiro