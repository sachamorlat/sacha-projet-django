from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Voyage(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    date_depart = models.DateTimeField(blank=False, default=timezone.now)
    date_arrivee = models.DateTimeField(blank=False, default=timezone.now)
    lieu_depart = models.CharField(max_length=100, blank=False)
    lieu_arrivee = models.CharField(max_length=100, blank=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_retour = models.DateTimeField(blank=True, null=True)

    def is_aller_simple(self):
        return self.date_retour is None

    def __str__(self):
        return self.nom

class Hebergement(models.Model):
    HOTEL = 'HO'
    AUBERGE = 'AU'
    CHAMBRE_HOTE = 'CH'
    HÉBERGEMENT_CHOICES = [
        (HOTEL, 'Hôtel'),
        (AUBERGE, 'Auberge'),
        (CHAMBRE_HOTE, 'Chambre d\'hôte'),
    ]
    
    nom = models.CharField(max_length=100, blank=False)
    type_hebergement = models.CharField(max_length=2, choices=HÉBERGEMENT_CHOICES, blank=False)
    ville = models.CharField(max_length=100, blank=False)
    adresse = models.CharField(max_length=200, blank=False) 
    prix_nuit = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    nombre_chambres_disponibles = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, null=True, blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    places_reservees = models.PositiveIntegerField(default=1)
    hebergement = models.ForeignKey(Hebergement, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.voyage.nom}"
