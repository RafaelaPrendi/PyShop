from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="index"),
    path('home/', views.homeview, name="homeview"),
    path(r'produkt/<int:id>/', views.produkt, name='produkt'),
    path(r'dyqan/<int:id>/', views.dyqan, name='dyqan'),
    path(r'dyqan/<int:id>/inventar/', views.inventar, name='inventar'),
    path('accounts/sign_up/', views.sign_up, name='sign_up'),
    path('accounts/login/', views.login_request, name='login_request'),
    path('accounts/logged_out/', views.logout_request, name="logout_request"),
    path(r'home/KerkoDyqan/', views.kerko_dyqan, name='kerko_dyqan'),
    path(r'home/KerkoProdukt/', views.kerko_produkt, name='kerko_produkt'),
    path(r'home/bli/', views.shto_ne_shporte, name='shto_ne_shporte'),

]