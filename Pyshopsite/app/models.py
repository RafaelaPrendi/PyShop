from django.db import models

class Produkt(models.Model):
    iid = models.IntegerField(primary_key=True)
    emri = models.CharField(max_length=128)
    kategoria = models.CharField(max_length=255)
    cmimi = models.FloatField()
    sasia = models.PositiveIntegerField(default=50)  # sasi default
    gjendje = models.BooleanField(default=True)
    dyqani = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.emri

    def as_dict(self):
        return {
            "emri": self.emri,
            "kategoria": self.kategoria,
            "cmimi": self.cmimi,
            "sasia": self.sasia,
            "gjendje": self.gjendje,
        }

class Dyqan(models.Model):
    iid = models.IntegerField(primary_key=True)
    emri = models.CharField(max_length=128)
    adresa = models.TextField()
    logo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, default="anonim@anonim.com")
    produktet = models.ManyToManyField(Produkt)

    def __str__(self):
        return self.emri

    def as_dict(self):
        return {
            "emri": self.emri,
            "adresa": self.adresa,
            "logo": self.logo,
        }
