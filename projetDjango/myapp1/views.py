from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Voyage, Reservation
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/inscription.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect.')
    return render(request, 'registrattion/login.html')

@login_required
def user_logout(request):
    if request.method == 'GET':  # Vérifiez la méthode HTTP
        logout(request)
        return redirect('login')  # Rediriger vers la page de connexion après déconnexion
    else:
        return HttpResponseNotAllowed(['GET'])


def rechercher_voyages(request):
    if request.method == 'POST':
        lieu_depart = request.POST.get('lieu_depart')
        lieu_arrivee = request.POST.get('lieu_arrivee')
        date_depart = request.POST.get('date_depart')
        voyages = Voyage.objects.filter(lieu_depart=lieu_depart, lieu_arrivee=lieu_arrivee, date_depart=date_depart)
        return render(request, 'recherche_voyages.html', {'voyages': voyages})
    else:
        return render(request, 'recherche_voyages.html')

@login_required
def reserver_voyage(request, voyage_id):
    voyage = Voyage.objects.get(pk=voyage_id)
    if request.method == 'POST':
        places_reservees = int(request.POST.get('places_reservees'))
        reservation = Reservation(voyage=voyage, utilisateur=request.user, places_reservees=places_reservees)
        reservation.save()
        return HttpResponseRedirect(reverse('voyages:detail_voyage', args=(voyage.id,)))
    else:
        return render(request, 'reserver_voyage.html', {'voyage': voyage})
