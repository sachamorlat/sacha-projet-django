from django.shortcuts import render
from .models import Voyage, Reservation
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def index(request):
    return render(request, 'index.html')

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index.html')  # Rediriger vers la page d'accueil après l'inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

@login_required    
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