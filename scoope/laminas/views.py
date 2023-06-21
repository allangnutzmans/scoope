from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Laminas, Estruturas
'''
def main(request):
    lamina_list = Laminas.objects.order_by()
    context = {
        "lamina_list": lamina_list
        }
    return render(request, 'main.html', context)

#def laminas(request, id):
    mylamina = Laminas.objects.filter(id=id)
    myestrutura = Estruturas.objects.all().values()
    template = loader.get_template('laminas.html')
    context = { 
        'mylamina': mylamina,
        'myestrutura' : myestrutura,
        }
    return HttpResponse(template.render(context, request))

def index(request):
    lamina_list = Laminas.objects.order_by()
    context = {
        "lamina_list": lamina_list
        }
    return render(request, 'master.html', context)
'''
def detail(request, laminas_id):
    lamina = get_object_or_404(Laminas, pk=laminas_id)
    lamina_list = Laminas.objects.order_by()
    context = {
        "lamina":lamina,
        "lamina_list": lamina_list
        }
    return render(request, 'laminas.html', context)
