import requests


def get_weather(city):
    api_key = "d7be19831f58519d2895a7d130af08cb"  # Reemplaza con tu clave de API

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&lang=es&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       wind = data['wind']
       weather_description = data['weather'][0]['description'] 
    
       return {
            "city": data['name'],
            "temperature": main['temp'],
            "pressure": main['pressure'],
            "humidity": main['humidity'],
            "wind_speed": wind['speed'],
            "description": weather_description
        }
    else:
        # Manejo de errores si la ciudad no se encuentra    
        return {"error": "Ciudad no encontrada"}

#print(get_weather())  # Ejemplo de llamada a la función

