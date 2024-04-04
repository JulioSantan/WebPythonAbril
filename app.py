from flask import Flask

app = Flask("olá")

@app.route('/')
def ola():
    return "Olá mundo"