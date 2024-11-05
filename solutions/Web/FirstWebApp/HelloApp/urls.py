from django.urls import path
from .views import home, about,contact,catalog,flowers,customers,login,register

urlpatterns=[
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('catalog', catalog, name='catalog'),
    path('flowers', flowers, name='flowers'),
    path('customers', customers, name='customers'),
    path('login', login, name='login'),  #step 5
    path('register', register, name='register'),
]