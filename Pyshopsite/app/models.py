from django.db import models

# Create your models here.

class Dyqan(models.Model):
    _id = models.IntegerField(primary_key=True)
    emri = models.CharField(max_length=255)
    adresa = models.TextField()
    logo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,default="anonim@anonim.com")

    def as_dict(self):
        return {
            "emri": self.emri,
            "adresa": self.adresa,
            "logo": self.logo,
        }

class Produkt(models.Model):
    _id = models.IntegerField(primary_key=True)
    emri = models.CharField(max_length=255)
    kategoria = models.CharField(max_length=255)
    cmimi = models.FloatField()
    # nje produkt mund te jete ne dis dyqane, disa dyqane mund ta kene kete produkt
    dyqani = models.ManyToManyField(Dyqan)
    #gjendje, sasia, dateSkadence#

    def as_dict(self):
        return {
            "emri": self.emri,
            "kategoria": self.kategoria,
            "cmimi": self.cmimi,

        }

