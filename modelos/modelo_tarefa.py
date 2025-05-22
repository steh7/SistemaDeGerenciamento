class ModeloTarefa:
    def __init__(self, id, titulo, descricao, data_vencimento, status, prioridade, usuario_uid):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.status = status
        self.prioridade = prioridade
        self.usuario_uid = usuario_uid
