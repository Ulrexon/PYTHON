import os
from flask import Flask, request
from twilio.rest import Client

def create_app():
    app = Flask(__name__)

    # Determinar el entorno
    env = os.getenv('FLASK_ENV', 'local')
    if env == 'development':
        app.config.from_object('config.development.Config')
    elif env == 'production':
        app.config.from_object('config.production.Config')
    else:
        app.config.from_object('config.local.Config')

    # Configurar las credenciales de Twilio
    account_sid = app.config['ACCOUNT_SID']
    auth_token = app.config['AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    # Ruta básica para verificar que el servidor esté funcionando
    @app.route('/')
    def index():
        return "Servidor Flask funcionando!"

    # Función para enviar un mensaje de WhatsApp
    def send_whatsapp_message(to, body):
        message = client.messages.create(
            body=body,
            from_=app.config['WHATSAPP_NUMBER'],  # Número de WhatsApp proporcionado por Twilio
            to=to
        )
        return message.sid

    # Endpoint para recibir mensajes de WhatsApp
    @app.route('/whatsapp', methods=['POST'])
    def whatsapp_webhook():
        from_number = request.values.get('From', None)
        body = request.values.get('Body', None)

        # Verificar si es el primer mensaje del usuario
        if is_first_message(from_number):
            response_message = "Bienvenido a nuestro servicio de WhatsApp!"
        else:
            response_message = get_chatbot_response(body)

        send_whatsapp_message(from_number, response_message)
        return '', 200

    # Función para verificar si es el primer mensaje del usuario
    def is_first_message(from_number):
        # Aquí debes implementar la lógica para verificar si es el primer mensaje
        # Podrías usar una base de datos para guardar los números y sus mensajes
        pass

    # Función para obtener la respuesta del chatbot
    def get_chatbot_response(message):
        # Aquí debes implementar la lógica para obtener la respuesta de tu chatbot
        # Podrías llamar a tu chatbot y pasarle el mensaje para obtener la respuesta
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
