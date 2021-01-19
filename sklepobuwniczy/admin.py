from django.contrib import admin

# Register your models here.
from sklepobuwniczy.models import Egzemplarze, Zakupy

admin.site.register(Egzemplarze)
admin.site.register(Zakupy)