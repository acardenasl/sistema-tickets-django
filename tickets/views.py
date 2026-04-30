from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import TicketForm
from .models import Ticket


class CustomLoginView(LoginView):
    template_name = "tickets/login.html"
    redirect_authenticated_user = True

#login y logout del user
@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("mis_tickets")

#crear ticket con el forms
@login_required
def crear_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user
            ticket.save()
            return redirect("mis_tickets")
    else:
        form = TicketForm()

    return render(request, "tickets/crear_ticket.html", {"form": form})

#mirar la lista de tickets creados por el
@login_required
def mis_tickets(request):
    tickets = Ticket.objects.filter(usuario=request.user)

    return render(request, "tickets/mis_tickets.html", {"tickets": tickets})

#mirar un ticket en especial creado por el
@login_required
def detalle_ticket(request, id_ticket):
    ticket = get_object_or_404(
        Ticket,
        id=id_ticket,
        usuario=request.user
    )

    return render(request, "tickets/detalle_ticket.html", {"ticket": ticket})