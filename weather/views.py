from django.shortcuts import render
import requests
from .models import City
from .forms import Cityfrom

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b2d4e63073666b3ae1090adbd46a93dd'

    if (request.method == 'POST'):
        form = Cityfrom(request.POST)
        form.save()
    
    form = Cityfrom()

    cities = City.objects.all()
    info_all = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
        'city': city.name,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
        }
        info_all.append(city_info)

    context = {'all_info': info_all, 'form': form}

    return render(request, 'weater/index.html', context)
