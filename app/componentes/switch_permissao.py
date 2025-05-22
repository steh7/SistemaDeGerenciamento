from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty

class SwitchPermissao(BoxLayout):
    permissao = StringProperty()
    valor = BooleanProperty()

    def __init__(self, permissao, valor_inicial, callback, **kwargs):
        super().__init__(**kwargs)
        self.permissao = permissao
        self.valor = valor_inicial
        self.callback = callback  # função que será chamada quando mudar

    def alternar(self):
        self.valor = not self.valor
        print(f"Permissão '{self.permissao}' alterada para {self.valor}")
        self.callback(self.permissao, self.valor)
