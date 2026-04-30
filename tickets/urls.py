from django.urls import path

from .views import (
    CustomLoginView,
    crear_ticket,
    detalle_ticket,
    logout_view,
    mis_tickets,
)


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("ticket/crear/", crear_ticket, name="crear_ticket"),
    path("mis-tickets/", mis_tickets, name="mis_tickets"),
    path("mis-tickets/<int:id_ticket>/", detalle_ticket, name="detalle_ticket"),
]