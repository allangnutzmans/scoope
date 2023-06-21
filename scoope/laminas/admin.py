from django.contrib import admin
from .models import Laminas, Estruturas

class LaminasAdmin(admin.ModelAdmin):
    list_display = ("nome_lamina", "montagem", "aumento", "corte", "coloracao")
    readonly_fields = ('id',)

class EstruturasAdmin(admin.ModelAdmin):
    list_display = ("nome_estrutura", "lamina")
    readonly_fields = ('id',)

admin.site.register(Laminas, LaminasAdmin)
admin.site.register(Estruturas, EstruturasAdmin)
