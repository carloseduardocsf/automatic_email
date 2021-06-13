#!/usr/bin/env python
# coding: utf-8

# In[17]:


import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá</p>
    <p>Segue meu primeiro email automático.</p>
    <p>Abs</p>
    <p>Cadu</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Email Automático"
    msg['From'] = 'caducavalcanti01@gmail.com'
    msg['To'] = 'caducavalcanti01@gmail.com'
    password = 'minha_senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[18]:


enviar_email()



