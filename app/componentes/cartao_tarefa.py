from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class CartaoTarefa(BoxLayout):
    titulo = StringProperty()
    descricao = StringProperty()
    data_vencimento = StringProperty()
    prioridade = StringProperty()
    status = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"Status da tarefa alterado para: {novo_status}")
