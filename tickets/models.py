from django.db import models

# Create your models here.
#Crear clases de categoria y ticket con sus atributos y reqs
from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Ticket(models.Model):
    ESTADO_ABIERTO = "abierto"
    ESTADO_EN_ESPERA = "en_espera"
    ESTADO_APROBADO = "aprobado"
    ESTADO_RECHAZADO = "rechazado"

    ESTADOS = [
        (ESTADO_ABIERTO, "Abierto"),
        (ESTADO_EN_ESPERA, "En espera"),
        (ESTADO_APROBADO, "Aprobado"),
        (ESTADO_RECHAZADO, "Rechazado"),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="tickets"
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_ABIERTO
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respuesta_admin = models.TextField(blank=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo