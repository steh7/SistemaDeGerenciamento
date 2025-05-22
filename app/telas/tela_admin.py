from kivy.uix.screenmanager import Screen
from app.servico_firebase import banco

class TelaAdmin(Screen):
    def listar_membros(self):
        membros = banco.collection('usuarios').where('perfil', '==', 'membro').stream()
        for membro in membros:
            print(membro.to_dict())

    def alterar_permissao(self, membro_uid, nova_permissao):
        banco.collection('usuarios').document(membro_uid).update({'permissoes': nova_permissao})
        print("Permissão atualizada com sucesso!")
