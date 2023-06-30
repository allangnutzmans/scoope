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
