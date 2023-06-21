from django.shortcuts import render, get_object_or_404
from .models import Laminas


def detail(request, laminas_id):
    lamina = get_object_or_404(Laminas, pk=laminas_id)
    lamina_list = Laminas.objects.order_by()
    context = {
        "lamina":lamina,
        "lamina_list": lamina_list
        }
    return render(request, 'laminas.html', context)

'''
#Class Based View
class LaminasListView(ListView):
    queryset = Laminas.objects.all()
    template_name = "laminas_list.html"
#    def get_context_data(self, **kwargs):
#        context = super(LaminasListView).get_context_data(**kwargs)
#        print(context)
#        return context
        

#Function Based View
def Laminas_list_view(request):
    queryset = Laminas.objects.all()
    context = {
        'lamina_list' : queryset
    }
    return render(request, 'laminas_list.html', context)

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

