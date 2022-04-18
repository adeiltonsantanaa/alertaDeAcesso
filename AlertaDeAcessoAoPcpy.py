import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from datetime import date, datetime
import os

def pegar_hora_atual():
    data_atual = datetime.now()
    data_em_texto = (f"dia {data_atual.strftime('%d/%m/%y')} exatamente às {data_atual.strftime('%H:%M:%S')}")
    return data_em_texto
def pegar_usuario_logado():
    user = (os.getlogin())
    return user
def enviar_email():
    emailEnvio = "###SEU E-MAIL###"
    senhaEmailEnvio = "###CREDENCIAL SMTP###"
    enviarDe = "###E-MAIL QUE VAI ENVIAR###"
    enviarPara = "###E-MAIL QUE VAI RECEBER###"
    tituloEmail = "Alguém Acessou Seu PC"
    corpoEmail = ("Olá, mestre. Como está o seu descanso?\nHoje {} o seu PC foi acessado pelo usuário {}".format(pegar_hora_atual(), pegar_usuario_logado()))

    mimemsg = MIMEMultipart()
    mimemsg['From']=enviarDe
    mimemsg['To']=enviarPara
    mimemsg['Subject']=tituloEmail
    mimemsg.attach(MIMEText(corpoEmail, 'plain'))
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(emailEnvio,senhaEmailEnvio)
    connection.send_message(mimemsg)
    connection.quit


if pegar_usuario_logado() != 'adeilton.filho1':
    enviar_email()
      
else:
    print("Usuário Autorizado!")
