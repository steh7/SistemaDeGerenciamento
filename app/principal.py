from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from telas.tela_login import TelaLogin
from telas.tela_cadastro import TelaCadastro
from telas.tela_principal import TelaPrincipal
from telas.tela_admin import TelaAdmin

class AplicativoGerenciador(App):
    def build(self):
        gerenciador_telas = ScreenManager()
        gerenciador_telas.add_widget(TelaLogin(name='login'))
        gerenciador_telas.add_widget(TelaCadastro(name='cadastro'))
        gerenciador_telas.add_widget(TelaPrincipal(name='principal'))
        gerenciador_telas.add_widget(TelaAdmin(name='admin'))
        return gerenciador_telas

if __name__ == '__main__':
    AplicativoGerenciador().run()
