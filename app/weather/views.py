from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from weather.models import City
from weather.forms import CityForm
import requests


def index_view(request):
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'pk': city.pk,
            'temperature': int(((r['main']['temp']) - 32) * 5/9),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)
    context = {
        'weather_data': weather_data,
    }
    return render(request, 'weather/index.html', context)



def create_view(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                    return redirect('weather:index')
                else:
                    err_msg = 'City does not exist in the world'
            else:
                err_msg = 'City already exist in the database!'
        if err_msg:
            message = err_msg
            message_class = 'alert alert-danger'
    form = CityForm
    context = {
        'form': form,
        'message': message,
        'message_class': message_class
    }
    return render(request, 'weather/form.html', context)


def destroy_view(request, pk):
    note = get_object_or_404(City, id=pk)
    note.delete()
    return redirect('weather:index')

