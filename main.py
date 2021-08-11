from flask import Flask
app=Flask(__name__)

@app.router('/')
def index():
    return "Esto es una prueba"

app.run()

