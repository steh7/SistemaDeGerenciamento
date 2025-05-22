from kivy.uix.screenmanager import Screen
from app.servico_firebase import criar_usuario

class TelaCadastro(Screen):
    def fazer_cadastro(self, email, senha, nome):
        try:
            criar_usuario(email, senha, nome, "membro", None, {
                "criar_tarefas": True,
                "editar_tarefas": True,
                "excluir_tarefas": False
            })
            print("Usuário cadastrado com sucesso!")
            self.manager.current = 'login'
        except:
            print("Erro ao cadastrar usuário")
