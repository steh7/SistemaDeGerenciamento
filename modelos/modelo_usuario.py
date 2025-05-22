class ModeloUsuario:
    def __init__(self, uid, nome, email, perfil, responsavel_uid, permissoes):
        self.uid = uid
        self.nome = nome
        self.email = email
        self.perfil = perfil
        self.responsavel_uid = responsavel_uid
        self.permissoes = permissoes
