from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Uzivatel(AbstractUser):
    telefon = models.CharField(max_length=15, unique=True)
    profilovy_obrazek = models.ImageField(upload_to='profily/', null=True, blank=True)

    def __str__(self):
        return self.username
    
class BankovniUcet(models.Model):
    TYPY_UCTU =(
        ('bezny', 'Běžný účet'),
        ('sporici', 'Spořící ůčet'),
        ('investicni', 'Investiční účet')
    )
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)
    cislo_uctu = models.CharField(max_length=20, unique=True)
    zustatek = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    typ_uctu = models.CharField(max_length=20, choices=TYPY_UCTU, default='bezny')

    def __str__(self):
        return f'{self.uzivatel.username} - {self.cislo_uctu}'

# Create your models here.
