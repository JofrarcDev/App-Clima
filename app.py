from flask import Flask, render_template, request  # Agrega 'request' aquí
import requests
from clima import get_weather  # Importando la función get_weather del archivo clima.py

def create_app():
    app = Flask(__name__) # creando la instancia de la aplicación Flask un objeto de la clase Flask

    @app.route('/')  # decorador que define la ruta de la aplicación
    def index():
        return render_template('index.html')  # renderiza el archivo index.html en la carpeta templates

    @app.route('/weather', methods=['POST'])
    def weather():
        city = request.form['city']  # Usa 'request' en vez de 'requests'
        weather_data = get_weather(city)
            
        if weather_data:
            return render_template('weather.html', weather=weather_data, city=city)
        else:
            return render_template('index.html', error="Ciudad no encontrada")
            # ruta para obtener el clima de una ciudad específica
            # ...existing code...
    return app
if __name__ == '__main__':
    app = create_app()
    app.run()  # Ejecuta la aplicación en modo de depuración