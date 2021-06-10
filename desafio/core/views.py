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
    print(pix_times)
    print(ted_times)
    context = {
        'pix': json.dumps(pix_times),
        'ted': json.dumps(ted_times),
        'dados': dados
    }
    return render(request, "index.html", context)