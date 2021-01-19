from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from sklepobuwniczy.models import Przedmioty, Egzemplarze, Rodzaje, Zakupy


def index(request):
    listaprzedmiotow = Przedmioty.objects.all()
    template = loader.get_template('home.html')
    context = {
        'listaprzedmiotow': listaprzedmiotow,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    return redirect('/')


@csrf_exempt
def checkout(request):
    template = loader.get_template('checkout.html')
    listamenugorne = ["Damskie", "Dzieciece", "Akcesoria", "images/srodkowy.jpg"]
    context = {'listamenugorne': listamenugorne}
    if request.method == 'POST':
        listanazw=[]
        for i in range(int(request.POST['itemCount'])):
            listanazw.append(str.strip(request.POST["item_name_"+str(i+1)]))
        listaprzedmiotow=[]
        print(len(listanazw))
        for przed in Przedmioty.objects.all():
            if przed.nazwa_przedmiotu in listanazw:
                listaprzedmiotow.append(przed)
        print(len(listaprzedmiotow))
        listaegzemplarzy=[]
        for egz in Egzemplarze.objects.all():
            if egz.getprzedmiot() in listaprzedmiotow:
                listaegzemplarzy.append(egz)
        print(len(listaegzemplarzy))
        zakup = Zakupy()
        zakup.id_uzytkownik=request.user.id;
        Zakupy.save(zakup)
        zakup = Zakupy.objects.last()
        for egz in listaegzemplarzy:
            egz.id_zakup = zakup.id_zakup
            egz.status_egzemplarza = "SPRZEDANY"
            Egzemplarze.save(egz)
        return redirect("/zakupy/")
    return HttpResponse(template.render(context, request))


def budowa(request):
    template = loader.get_template('budowa.html')
    context = {}
    return HttpResponse(template.render(context, request))

def zakupy(request):
    template = loader.get_template('zakupy.html')
    listamenugorne = ["Damskie", "Dzieciece", "Akcesoria", "images/srodkowy.jpg"]
    lista=[]
    for zakup in Zakupy.objects.all():
        if zakup.id_uzytkownik==request.user.id:
            lista.append(zakup)

    context = {
        'lista': lista,
        'listamenugorne': listamenugorne,
    }
    return HttpResponse(template.render(context, request))



def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if not form.is_valid():
            tekst = "haslo jest za słabe!"
            return render(response, "registration/register.html", {"form": form, 'tekst': tekst})
        if form.is_valid():
            form.save()
            return redirect("/login/")
        return render(response, "registration/register.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(response, "registration/register.html", {"form": form})


def obuwiemeskie(request):
    lista = []
    for egzemplarz in Egzemplarze.objects.all():
        if egzemplarz.getprzedmiot().getrodzaj_producent().getrodzaj().gettyp().typ_nazwa == "Meskie":
            lista.append(egzemplarz)
    listarodzaje = []
    for rodzaj in Rodzaje.objects.all():
        if rodzaj.gettyp().typ_nazwa == "Meskie":
            listarodzaje.append(rodzaj)
    listaproducenci = []
    for egzemplarz in lista:
        listaproducenci.append(egzemplarz.getprzedmiot().getrodzaj_producent().getproducent())
    listamenugorne = ["Damskie", "Dzieciece", "Akcesoria", "images/srodkowy.jpg"]
    template = loader.get_template('obuwie.html')
    context = {
        'lista': lista,
        'listamenugorne': listamenugorne,
        'listaproducenci': set(listaproducenci),
        'listarodzaje': listarodzaje,
    }
    return HttpResponse(template.render(context, request))

def obuwiedamskie(request):
    lista = []
    for egzemplarz in Egzemplarze.objects.all():
        if egzemplarz.getprzedmiot().getrodzaj_producent().getrodzaj().gettyp().typ_nazwa == "Damskie":
            lista.append(egzemplarz)
    listarodzaje = []
    for rodzaj in Rodzaje.objects.all():
        if rodzaj.gettyp().typ_nazwa == "Damskie":
            listarodzaje.append(rodzaj)
    listaproducenci = []
    for egzemplarz in lista:
        listaproducenci.append(egzemplarz.getprzedmiot().getrodzaj_producent().getproducent())
    listamenugorne = ["Meskie", "Dzieciece", "Akcesoria", "images/srodkowy.jpg"]
    template = loader.get_template('obuwie.html')
    context = {
        'lista': lista,
        'listamenugorne': listamenugorne,
        'listaproducenci': set(listaproducenci),
        'listarodzaje': listarodzaje,
    }
    return HttpResponse(template.render(context, request))

def obuwiedzieciece(request):
    lista = []
    for egzemplarz in Egzemplarze.objects.all():
        if egzemplarz.getprzedmiot().getrodzaj_producent().getrodzaj().gettyp().typ_nazwa == "Dzieciece":
            lista.append(egzemplarz)
    listarodzaje = []
    for rodzaj in Rodzaje.objects.all():
        if rodzaj.gettyp().typ_nazwa == "Dzieciece":
            listarodzaje.append(rodzaj)
    listaproducenci = []
    for egzemplarz in lista:
        listaproducenci.append(egzemplarz.getprzedmiot().getrodzaj_producent().getproducent())
    listamenugorne = ["Damskie", "Meskie", "Akcesoria", "images/srodkowy.jpg"]
    template = loader.get_template('obuwie.html')
    context = {
        'lista': lista,
        'listamenugorne': listamenugorne,
        'listaproducenci': set(listaproducenci),
        'listarodzaje': listarodzaje,
    }
    return HttpResponse(template.render(context, request))


