from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.


def home(request):
    if 'city' in request.POST:
        city= request.POST['city']
    else:
        city= 'Nairobi'
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid=f4c712fc16d237163c20cb817d9de848'
    params = {'units':'merits'}

    API_KEY =  'AIzaSyCSEIX3ABiK8eqPYj13q-IpZCsCDSEbJDM'

    SEARCH_ENGINE_ID = 'f2d7b5407d04c4144'
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"


    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    

    try:
         data = requests.get(url, params).json()

         description = data['weather'][0]['description']
         icon = data['weather'][0]['icon']
         temp = data['main']['temp']

         day = datetime.date.today()

         return render(request,'home.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url': image_url})

    except:
        exception_occurred= True
        messages.error(request,'invalid data')
        day = datetime.date.today()

        return render(request,'home.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'Nairobi' , 'exception_occurred':exception_occurred } )
