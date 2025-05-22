import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"

    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())
