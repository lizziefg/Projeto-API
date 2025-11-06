from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# 1. Inicialização da aplicação FastAPI
app = FastAPI()

# 2. Definição do modelo de dados para um Processo
class Processo(BaseModel):
    numero: str
    autor: str
    reu: str
    status: str

# 3. Criação de um "banco de dados" em memória como um dicionário
db_processos: Dict[str, Processo] = {}

# --- Endpoints da API ---
# Endpoint para criar um novo processo (CREATE)
@app.post("/processos/", response_model=Processo, status_code=201)
def criar_processo(processo: Processo):
    if processo.numero in db_processos:
        raise HTTPException(status_code=400, detail="Processo com este número já existe")
    db_processos[processo.numero] = processo
    return processo

# Endpoint para ler um processo específico (READ)
@app.get("/processos/{numero_processo}", response_model=Processo)
def ler_processo(numero_processo: str):
    if numero_processo not in db_processos:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    return db_processos[numero_processo]

# Endpoint para listar todos os processos (READ ALL)
@app.get("/processos/", response_model=List[Processo])
def listar_processos():
    return list(db_processos.values())

# Endpoint para deletar um processo (DELETE)
@app.delete("/processos/{numero_processo}", status_code=204)
def deletar_processo(numero_processo: str):
    if numero_processo not in db_processos:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    del db_processos[numero_processo]
    return {"detail": "Processo deletado com sucesso"}