from django.db import models
from django.contrib.auth.models import User


class Voyage(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    lieu_depart = models.CharField(max_length=100)
    lieu_arrivee = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    places_reservees = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.voyage.nom}"

class Itineraire(models.Model):
    voyage = models.OneToOneField(Voyage, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.voyage.nom