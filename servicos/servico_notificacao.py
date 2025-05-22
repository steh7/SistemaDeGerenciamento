from plyer import notification

def notificar_tarefa(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        timeout=10
    )
