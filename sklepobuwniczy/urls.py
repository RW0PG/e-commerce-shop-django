from django.urls import path

from . import views

urlpatterns = [
    path('obuwie-meskie/', views.obuwiemeskie, name='obuwie-meskie'),
    path('obuwie-damskie/', views.obuwiedamskie, name='obuwie-damskie'),
    path('obuwie-dzieciece/', views.obuwiedzieciece, name='obuwie-dzieciece'),
    path('', views.index, name='home'),
    path('register/', views.register, name='rejstracja'),
    path('budowa/', views.budowa, name='budowa'),
    path('obuwie-akcesoria/', views.budowa, name='budowa'),
    path('home/', views.home, name='homee'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout', views.checkout, name='checkout'),
    path('zakupy/', views.zakupy, name='zakupy')
]