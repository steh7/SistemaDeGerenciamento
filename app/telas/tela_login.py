from kivy.uix.screenmanager import Screen
from app.servico_firebase import autenticacao

class TelaLogin(Screen):
    def fazer_login(self, email, senha):
        try:
            usuario = autenticacao.sign_in_with_email_and_password(email, senha)
            self.manager.current = 'principal'
        except:
            print("Erro ao fazer login")
