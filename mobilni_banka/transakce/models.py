from django.db import models
from ucet.models import Uzivatel, BankovniUcet

class Transakce(models.Model):
    TYPY_TRANSAKCI = (
        ('prevod', 'Převod mezi účty'),
        ('platba', 'Platba'),
        ('vklad', 'Vklad'),
        ('vyber', 'Výběr'),
    )

    od_uzivatele = models.ForeignKey(Uzivatel, related_name='odeslane_transakce', on_delete=models.CASCADE)
    na_ucet = models.ForeignKey(BankovniUcet, on_delete=models.CASCADE)
    castka = models.DecimalField(max_digits=15, decimal_places=2)
    typ_transakce = models.CharField(max_length=20, choices=TYPY_TRANSAKCI)
    datum = models.DateTimeField(auto_now_add=True)
    popis = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.typ_transakce} - {self.castka} Kč"

# Create your models here.
