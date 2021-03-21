from django.shortcuts import render
from lookup.forms import SearchForm
from django.urls import reverse
import requests
from weather import settings

def home(request):
    try:    
        if request.method == 'POST':
            form = SearchForm(request.POST) # creating form instance
            if form.is_valid():
                zipcode = form.cleaned_data['zipcode']
                
            api_request = requests.get(f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY={settings.API}')
            
        else:
            form = SearchForm()
            api_request = requests.get(f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=43001&distance=25&API_KEY={settings.API}')
    except:
        api_request = []




    try:
        api = api_request.json()
        if api:
            if api[0]['Category']['Number'] == 1:
                background_color = "green-color"
                forecast_message = "(0-50) Enjoy your outdoor activities. It’s a great day to be active outside."
                
            if api[0]['Category']['Number'] == 2:
                background_color = "yellow-color"
                forecast_message = "(51-100) Unusually sensitive people: Consider reducing prolonged or heavy outdoor exertion. Watch for symptoms such as coughing or shortness of breath. These are signs to take it easier. Everyone else: It’s a good day to be active outside."
                
            if api[0]['Category']['Number'] == 3:
                background_color = "orange-color"
                forecast_message = "(101-150) Sensitive groups: Reduce prolonged or heavy outdoor exertion. Take more breaks, do less intense activities. Watch for symptoms such as coughing or shortness of breath. Schedule outdoor activities in the morning when ozone is lower. People with asthma should follow their asthma action plans and keep quick- relief medicine handy."
                
            if api[0]['Category']['Number'] == 4:
                background_color = "red-color"
                forecast_message = "(151-200) Sensitive groups: Avoid prolonged or heavy outdoor exertion. Schedule outdoor activities in the morning when ozone is lower. Consider moving activities indoors. People with asthma, keep quick-relief medicine handy. Everyone else: Reduce prolonged or heavy outdoor exertion. Take more breaks, do less intense activities. Schedule outdoor activities in the morning when ozone is lower. "

            if api[0]['Category']['Number'] == 5:
                background_color = "purple-color"
                forecast_message = "(201-300) Sensitive groups: Avoid all physical activity outdoors. Move activities indoors or reschedule to a time when air quality is better. People with sthma, keep quick-relief medicine handy. Everyone else: Avoid prolonged or heavy outdoor exertion. Schedule outdoor activities in the morning when ozone is lower. Consider moving activities indoors. "
                
            if api[0]['Category']['Number'] == 6:
                background_color = "maroon-color"
                forecast_message = "(301-500) Everyone: Avoid all physical activity outdoors. It's due to us (human)."

        else:
            api = "Error"
        return render(request, 'lookup/home.html', {'form': form , 'api': api, 'background_color': background_color , 'forecast_message': forecast_message})

        
    except:
        api =  "Error"
        return render(request, 'lookup/home.html', {'form': form , 'api': api})




def about(request):
    return render(request, 'lookup/about.html')