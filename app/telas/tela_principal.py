from kivy.uix.screenmanager import Screen
from app.servico_firebase import criar_tarefa

class TelaPrincipal(Screen):
    def criar_nova_tarefa(self, titulo, descricao, data_vencimento, prioridade, usuario_uid):
        criar_tarefa(titulo, descricao, data_vencimento, prioridade, usuario_uid)
        print("Tarefa criada com sucesso!")
