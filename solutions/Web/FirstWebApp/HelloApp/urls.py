from django.urls import path
from .views import home, about,contact,catalog,flowers,customers

urlpatterns=[
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('catalog', catalog, name='catalog'),
    path('flowers', flowers, name='flowers'),
    path('customers', customers, name='customers'),
]