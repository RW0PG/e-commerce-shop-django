# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Adresy(models.Model):
    id_adres = models.AutoField(db_column='ID_ADRES', unique=True, primary_key=True)  # Field name made lowercase.
    miasto = models.CharField(db_column='MIASTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    miejscowosc = models.CharField(db_column='MIEJSCOWOSC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wojewodztwo = models.CharField(db_column='WOJEWODZTWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    powiat = models.CharField(db_column='POWIAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kod_pocztowy = models.CharField(db_column='KOD_POCZTOWY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ulica = models.CharField(db_column='ULICA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nr_domu = models.CharField(db_column='NR_DOMU', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nr_lokalu = models.CharField(db_column='NR_LOKALU', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ADRESY'


class Egzemplarze(models.Model):
    id_egzemplarz = models.AutoField(db_column='ID_EGZEMPLARZ', unique=True, primary_key=True)  # Field name made lowercase.
    id_przedmiot = models.IntegerField(db_column='ID_PRZEDMIOT', blank=True, null=True)  # Field name made lowercase.
    id_zakup = models.IntegerField(db_column='ID_ZAKUP', blank=True, null=True)  # Field name made lowercase.
    rozmiar = models.IntegerField(db_column='ROZMIAR', blank=True, null=True)  # Field name made lowercase.
    kolor = models.CharField(db_column='KOLOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    status_egzemplarza = models.CharField(db_column='STATUS_EGZEMPLARZA', max_length=30, blank=True, null=True)  # Field name made lowercase.

    def getprzedmiot(self):
        return list(Przedmioty.objects.filter(id_przedmiot=self.id_przedmiot))[0]

    class Meta:
        db_table = 'EGZEMPLARZE'


class Kontakty(models.Model):
    id_kontakt = models.AutoField(db_column='ID_KONTAKT', unique=True, primary_key=True)  # Field name made lowercase.
    nr_tel = models.CharField(db_column='NR_TEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'KONTAKTY'


class Producenci(models.Model):
    id_producent = models.AutoField(db_column='ID_PRODUCENT', unique=True, primary_key=True)  # Field name made lowercase.
    nazwa_producenta = models.CharField(db_column='NAZWA_PRODUCENTA', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PRODUCENCI'


class Przedmioty(models.Model):
    id_przedmiot = models.AutoField(db_column='ID_PRZEDMIOT', unique=True, primary_key=True)  # Field name made lowercase.
    id_rodzaj_producent = models.IntegerField(db_column='ID_RODZAJ_PRODUCENT', blank=True, null=True)  # Field name made lowercase.
    zdjecia = models.CharField(db_column='ZDJECIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nazwa_przedmiotu = models.CharField(db_column='NAZWA_PRZEDMIOTU', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cena = models.IntegerField(db_column='CENA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PRZEDMIOTY'

    def getrodzaj_producent(self):
        return list(RodzajeProducenci.objects.filter(id_rodzaj_producent=self.id_rodzaj_producent))[0]


class Rodzaje(models.Model):
    id_rodzaj = models.AutoField(db_column='ID_RODZAJ', unique=True, primary_key=True)  # Field name made lowercase.
    rodzaj_nazwa = models.CharField(db_column='RODZAJ_NAZWA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_typ = models.IntegerField(db_column='ID_TYP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'RODZAJE'
    def gettyp(self):
        return list(Typy.objects.filter(id_typ=self.id_typ))[0]


class RodzajeProducenci(models.Model):
    id_rodzaj_producent = models.AutoField(db_column='ID_RODZAJ_PRODUCENT', unique=True, primary_key=True)  # Field name made lowercase.
    id_rodzaj = models.IntegerField(db_column='ID_RODZAJ', blank=True, null=True)  # Field name made lowercase.
    id_producent = models.IntegerField(db_column='ID_PRODUCENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'RODZAJE_PRODUCENCI'

    def getrodzaj(self):
        return list(Rodzaje.objects.filter(id_rodzaj=self.id_rodzaj))[0]

    def getproducent(self):
        return list(Producenci.objects.filter(id_producent=self.id_producent))[0]

class Typy(models.Model):
    id_typ = models.AutoField(db_column='ID_TYP', unique=True, primary_key=True)  # Field name made lowercase.
    typ_nazwa = models.CharField(db_column='TYP_NAZWA', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TYPY'



class Zakupy(models.Model):
    id_zakup = models.AutoField(db_column='ID_ZAKUP', unique=True, primary_key=True)  # Field name made lowercase.
    id_uzytkownik = models.IntegerField(db_column='ID_UZYTKOWNIK', blank=True, null=False)  # Field name made lowercase.
    status_zamowienia = models.CharField(db_column='STATUS_ZAMOWIENIA', max_length=30, default="PRZYJETE", blank=True, null=False)  # Field name made lowercase.

    class Meta:
        db_table = 'ZAKUPY'

    def calkowitawartosc(self):
        listaegz=[]
        for egz in Egzemplarze.objects.all():
            if(egz.id_zakup==self.id_zakup):
                listaegz.append(egz)
        wartosc=0;
        for egz in listaegz:
            wartosc = wartosc + egz.getprzedmiot().cena

        return wartosc
