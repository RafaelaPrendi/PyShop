from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    produktet = models.ManyToManyField(Produkt)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profil.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profil.save()