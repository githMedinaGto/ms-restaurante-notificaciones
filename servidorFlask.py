# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:27:46 2021

@author: Jonathan Medina
"""

# save this as app.py
from flask import Flask
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os 
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
 
@app.route("/email")
def enviarCorreo():
    hashString = request.args.get("hash")
    if(hashString == os.environ.get('SECURITY_HASH')):
        
        destino = request.args.get("correo_destino")
        asunto = request.args.get("asunto")
        mensaje = request.args.get("mensaje")
        
        message = Mail(
            from_email='racieljonathan@gmail.com',
            to_emails=destino,
            subject=asunto,
            html_content=mensaje)
        try:
            sg = SendGridAPIClient('Aqui va la API KEY de SEND GRID')
            response = sg.send(message)
            print("Enviado")
            return "OK"
        except Exception as e:
            print(e.message)
            return "OK"
    else:
        print("Sin hash")
        return "hash error"
        
if __name__ == '__main__':
    app.run()