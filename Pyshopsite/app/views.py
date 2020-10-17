from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,Http404, redirect, HttpResponse, HttpResponseRedirect
from . import models
from .models import Produkt, Dyqan, Profil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import DyqanForm, ProduktForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages import constants as messages
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'home.html')

def sign_up(request):
    data = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home.html')
    data['form'] = form
    return render(request, 'registration/sign_up.html', data)

def homeview(request):
    return render(request, 'home.html')

@require_http_methods(["GET"])
def produkt(request, id):
    produkti = get_object_or_404(models.Produkt, pk=id)
    data = {
        'produkt' : produkti,
         'titulli_i_faqes' : 'Produkti (id: {})'.format(id),

    }
    request.session['produkte'] = produkti
    #'dyqanet' : [dq.as_dict() for dq in Dyqan.objects.all()]
    return render(request, 'produkt.html', data)
    #paraqit produktin
    #dyqanet ku ndodhet produkti dhe cmimin

@require_http_methods(["GET"])
def dyqan(request, id):
    dyqani = get_object_or_404(models.Dyqan, pk=id)
    data = {
        'dyqan': dyqani,
        'titulli_i_faqes': 'Dyqani (id: {})'.format(id),
        'produktet': [p.as_dict() for p in dyqani.produktet.all()]
    }
    return render(request, 'dyqane.html', data)

def inventar(request, id):
    dyqani = get_object_or_404(models.Dyqan, pk=id)
    totali = 0
    kategoriTotal = {}
    for p in dyqani.produktet.all():
        totali += float(p.cmimi)
        kategoriTotal[p.kategoria] = 0

    for key in kategoriTotal:
        shumaKategori = 0
        prod = Produkt.objects.filter(kategoria=key)
        for p in prod:
            shumaKategori += float(p.cmimi)
        kategoriTotal[key] = shumaKategori

    data = {
        'dyqan': dyqani,
        'titulli_i_faqes': 'Dyqani (id: {})'.format(id),
        'totali': totali,
        'kategoriTotal': kategoriTotal
    }
    return render(request, 'inventar.html',data)
    # paraqit dyqanin
    # vlera tot e produkteve
    # vlera tot e kategorive

def kerko_dyqan(request):
    if request.method == 'POST':
        form = DyqanForm(request.POST)
        if form.is_valid():
            emri = form.cleaned_data['emri_dyqanit']

            try:
                dyqani = Dyqan.objects.filter(emri=emri)[0]
                data = {
                    'dyqan': dyqani,
                    'titulli_i_faqes': 'Dyqani (id: {})'.format(id),
                    'produktet': [p.as_dict() for p in dyqani.produktet.all()]
                }
                return render(request, 'dyqane.html', data)
            except ObjectDoesNotExist:
                raise Http404('Dyqani nuk eshte ne databazen tone.')
            #return HttpResponseRedirect('')
        else:
            return render(request, 'app/KerkoDyqan/', {'msg': 'ERROR'})
    else:
        form = DyqanForm()
        return render(request, 'KerkoDyqan.html', {'form': form})

def kerko_produkt(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST)
        if form.is_valid():
            emri = form.cleaned_data['emri_produktit']
            try:
                produkti = Produkt.objects.get(emri=emri)
                data = {
                    'produkt': produkti,
                    'titulli_i_faqes': 'Produkti (id: {})'.format(id),
                }
                return render(request, 'produkt.html', data)
            except ObjectDoesNotExist:
                raise Http404('Produkti nuk eshte ne databazen tone.')
            #return HttpResponseRedirect('')
        else:
            return render(request, '/KerkoProdukt/', {'msg': 'ERROR'})
    else:
        form = DyqanForm()
        return render(request,'KerkoProdukt.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user'] = user
                messages.info(request, f' You are now logged in as {{ username }}')
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='/accounts/login/')
def shto_ne_shporte(request):
    produktet = request.POST.getlist('produkt')
    request.session['produkte'] = produktet
    return render(request, 'bli.html', {'produkte':produktet})

@login_required(login_url='/accounts/login/')
def logout_request(request):
    auth.logout(request)
    return render(request, 'registration/logged_out.html')

@login_required(login_url='/accounts/login/')
def blerje(request):
    return render(request, 'sukses.html')
