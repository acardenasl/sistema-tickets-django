from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Categoria, Ticket

#CategoriaAdmin permite ver y buscar categorías desde el admin.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)


#TicketAdmin permite que el administrador vea tickets ordenados, filtre por estado/categoría/fecha y busque por título, descripción o usuario.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "usuario",
        "categoria",
        "estado",
        "fecha_creacion",
    )
    list_filter = (
        "estado",
        "categoria",
        "fecha_creacion",
    )
    search_fields = (
        "titulo",
        "descripcion",
        "usuario__username",
    )
    readonly_fields = (
        "usuario",
        "categoria",
        "titulo",
        "descripcion",
        "fecha_creacion",
    )
