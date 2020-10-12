import csv
from app.models import Produkt,Dyqan

def krijo_Produkt(_id,emri, kategoria, cmimi,dyqani):
    sasia = 50
    gjendje = True
    prod = Produkt.objects.create(
        iid=_id,
        emri=emri,
        kategoria=kategoria,
        cmimi=cmimi,
        sasia=sasia,
        gjendje=gjendje,
        dyqani=dyqani
    )
    return prod

def krijo_Dyqan(emri, adresa, logo, email,_id ):
    dyqan = Dyqan.objects.create(
        emri=emri,
        adresa=adresa,
        logo=logo,
        email=email,
        iid=_id
    )
    return dyqan

def krijo_lidhje(emri_Dyqani):
    prod = Produkt.objects.filter(dyqani=emri_Dyqani)
    for p in prod:
        dyqani = Dyqan.objects.filter(emri=emri_Dyqani.lower().title())
        for dq in dyqani:
            print("P eshte : ", p, 'D eshte : ', dq)
            dq.produktet.add(p)
            dq.save()
    #print('DYQANIIII', dyqani)

def krijo_Produktet():
    produktet = set()
    with open('data2.csv', 'r', encoding='utf8') as data:
        reader = csv.reader(data)
        for rresht in reader:
            iid = rresht[0]
            emri = rresht[1]
            kategoria = rresht[2]
            cmimi = rresht[3]
            dyqani = rresht[4]
            newProd = krijo_Produkt(iid, emri, kategoria, cmimi,dyqani)
            produktet.add(newProd)
    return produktet

def krijo_Dyqanet():
    dyqane = set()
    with open('data2.csv', 'r', encoding='utf8') as data:
        reader = csv.reader(data)
        for rresht in reader:
            iid = rresht[0]
            emri = rresht[4]
            adresa = rresht[5]
            logo = rresht[6]
            email = rresht[7]
            newDyqan = krijo_Dyqan(emri, adresa, logo, email, iid)
            dyqane.add(newDyqan)

    return dyqane

def krijo_lidhjet():
    with open('data2.csv', 'r', encoding='utf8') as data:
            reader = csv.reader(data)
            for rresht in reader:
                emer_dyqani = rresht[4]
                #id_prod = rresht[0]
                krijo_lidhje(emer_dyqani)
    print('lidhjet U KRIJUAN')


def zbraz():
    Produkt.objects.all().delete()
    Dyqan.objects.all().delete()

def nr_Produkteve():
    return Produkt.objects.all().count()

def nr_Dyqaneve():
    return Dyqan.objects.all().count()

def run():
    print("Pastrim i DB ...")
    zbraz()
    print('PRODUKTE Numri para :', nr_Produkteve())
    krijo_Produktet()
    print('PRODUKTE Numri pas :', nr_Produkteve())
    print('DYQANE Numri para :', nr_Dyqaneve())
    krijo_Dyqanet()
    print('DYQANE Numri pas :', nr_Dyqaneve())
    print('Krijo lidhjet')
    krijo_lidhjet()




