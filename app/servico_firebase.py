import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

configuracao = {
   "apiKey": "AIzaSyC11kw7g2Hok9NkNXnCsXQRs48kc3N_XSo",
    "authDomain": "gerenciador-py.firebaseapp.com",
    "databaseURL": "https://gerenciador-py.firebaseio.com",  # pode adicionar assim, padrão do Firebase
    "projectId": "gerenciador-py",
    "storageBucket": "gerenciador-py.firebasestorage.app",
    "messagingSenderId": "304067828965",
    "appId": "1:304067828965:web:214bf598e3e0beda9e080c"
}

firebase = pyrebase.initialize_app(configuracao)
autenticacao = firebase.auth()

credencial = credentials.Certificate("chaveFirebase.json")
firebase_admin.initialize_app(credencial)
banco = firestore.client()

def criar_usuario(email, senha, nome, perfil, responsavel_uid, permissoes):
    usuario = autenticacao.create_user_with_email_and_password(email, senha)
    uid = usuario['localId']
    dados_usuario = {
        'uid': uid,
        'email': email,
        'nome': nome,
        'perfil': perfil,
        'responsavel_uid': responsavel_uid,
        'permissoes': permissoes
    }
    banco.collection('usuarios').document(uid).set(dados_usuario)
    return uid

def criar_tarefa(titulo, descricao, data_vencimento, prioridade, usuario_uid):
    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'data_vencimento': data_vencimento,
        'prioridade': prioridade,
        'status': 'pendente',
        'usuario_uid': usuario_uid
    }
    banco.collection('tarefas').add(tarefa)

def verificar_permissao(usuario, acao):
    if usuario['perfil'] == 'admin':
        return True
    return usuario['permissoes'].get(acao, False)
