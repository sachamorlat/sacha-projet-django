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
            return redirect('login')  
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
            return render(request, 'authentification/login.html')
    elif request.method == 'GET':
        return render(request, 'authentification/login.html')

@login_required
def user_logout(request):
    if request.method == 'GET': 
        logout(request)
        return redirect('login')  
    else:
        return HttpResponseNotAllowed(['GET'])


def rechercher_voyages(request):
    if request.method == 'POST':
        lieu_depart = request.POST.get('lieu_depart')
        lieu_arrivee = request.POST.get('lieu_arrivee')
        date_depart = request.POST.get('date_depart')
        voyages = Voyage.objects.filter(Q(lieu_depart__icontains=lieu_depart) | 
                                         Q(lieu_arrivee__icontains=lieu_arrivee) | 
                                         Q(date_depart__icontains=date_depart))
        return render(request, 'rechercher_voyages.html', {'voyages': voyages})
    else:
        return render(request, 'rechercher_voyages.html')

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
