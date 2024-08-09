import os
from flask import Flask, request, jsonify
from twilio.rest import Client

def create_app():
    app = Flask(__name__)

    # Ruta básica para verificar que el servidor esté funcionando
    @app.route('/')
    def index():
        return "Servidor Flask funcionando!"

    # Función para verificar si es el primer mensaje del usuario
    def is_first_message(from_number):
        # Implementación básica que utiliza una variable en memoria.
        # En producción, deberías usar una base de datos.
        # Este ejemplo asume que es siempre el primer mensaje para fines demostrativos.
        # Debes reemplazar esto con una lógica real que verifique una base de datos.
        return True

    # Función para obtener la respuesta del chatbot
    def get_chatbot_response(message):
        # Implementación básica que devuelve una respuesta estática.
        # Aquí es donde integrarías tu lógica de chatbot real.
        return f"Echo: {message}"


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
