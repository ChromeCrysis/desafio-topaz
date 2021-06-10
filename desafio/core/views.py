from django.shortcuts import render
from core.models import Dado

import json

# Create your views here.
def index(request):
    dados = Dado.objects.all().order_by('-date_event')
    pix = Dado.objects.filter(event_type='PIX')
    pix_times = pix.count()
    ted = Dado.objects.filter(event_type='TED')
    ted_times = ted.count()

    #Contagem das localizações fora do habitual
    location1 = Dado.objects.filter(longitude= '-49.27759092402380', latitude='-16.698270789801')
    location2 = Dado.objects.filter(longitude= '-49.2775909297327', latitude='-16.698270788567500')
    location3 = Dado.objects.filter(longitude= '-49.277590956', latitude='-16.698270788852300')
    location4 = Dado.objects.filter(longitude= '-49.277590924234', latitude='-16.69827078881230')
    locations_count = location1.count() + location2.count() + location3.count() + location4.count()
    total_locations = dados.count()
    
    context = {
        'pix': json.dumps(pix_times),
        'ted': json.dumps(ted_times),
        'location': json.dumps(locations_count),
        'total_location': json.dumps(total_locations),
        'dados': dados
    }
    return render(request, "index.html", context)