from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .servico_firebase import criar_usuario, criar_tarefa

app = FastAPI()

# Modelos para entrada de dados
class Usuario(BaseModel):
    email: str
    senha: str
    nome: str
    perfil: str
    responsavel_uid: str
    permissoes: dict

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    data_vencimento: str
    prioridade: str
    usuario_uid: str

@app.post("/usuario/")
def api_criar_usuario(usuario: Usuario):
    uid = criar_usuario(
        usuario.email,
        usuario.senha,
        usuario.nome,
        usuario.perfil,
        usuario.responsavel_uid,
        usuario.permissoes
    )
    if not uid:
        raise HTTPException(status_code=400, detail="Erro ao criar usuário")
    return {"uid": uid}

@app.post("/tarefa/")
def api_criar_tarefa(tarefa: Tarefa):
    try:
        criar_tarefa(
            tarefa.titulo,
            tarefa.descricao,
            tarefa.data_vencimento,
            tarefa.prioridade,
            tarefa.usuario_uid
        )
        return {"mensagem": "Tarefa criada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
