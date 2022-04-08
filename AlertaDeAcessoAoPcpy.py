import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from datetime import date, datetime
import os

user = (os.getlogin())

if user != 'adeilton.filho':
    data_atual = datetime.now()
    data_em_texto = data_atual.strftime('%d/%m/%y')
    hora_acesso = data_atual.strftime('%H:%M:%S')

    emailEnvio = "###SEU E-MAIL###"
    senhaEmailEnvio = "###CREDENCIAL SMTP###"
    enviarDe = "###E-MAIL QUE VAI ENVIAR###"
    enviarPara = "###E-MAIL QUE VAI RECEBER###"
    tituloEmail = "Alguém Acessou Seu PC"
    corpoEmail = ("Olá, mestre. Como está o seu descanso?\nHoje dia {} exatamente às {} o seu PC foi acessado pelo usuário {}".format(data_em_texto, hora_acesso,user))

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
else:
    print("Usuário Autorizado!")