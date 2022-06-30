from django.shortcuts import render
import json
import requests

def index(request):
    return render(request, 'index.html')

def weather(request):
    if request.method == 'POST':
        # collect data from index and instantiate to city
        city = request.POST['city']

        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid={api_key}')
        # converting the response to json data
        json_data = response.json()

        #creating a dictionary with the json_data for reference in the templates
        data = {
            "country" : str(json_data['name']),
            "country_code" : str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }

    context = {
        'city': city, 'data': data
    }
    return render(request, 'weather.html', context)
