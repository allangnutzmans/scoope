from django.shortcuts import render
from laminas.models import Laminas

def main(request):
    lamina_list = Laminas.objects.order_by()
    context = {
        "lamina_list": lamina_list
        }
    return render(request, 'main.html', context)

def index(request):
    lamina_list = Laminas.objects.order_by()
    context = {
        "lamina_list": lamina_list
        }
    return render(request, 'master.html', context)

