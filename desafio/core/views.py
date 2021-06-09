from django.shortcuts import render
from core.models import Dado

# Create your views here.
def index(request):
    dados = Dado.objects.all().order_by('-date_event')
    print(dados)
    context = {
        'dados': dados
    }
    return render(request, "index.html", context)