from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from .models import Customer, Product

#action methods


def home(request):
    #return HttpResponse("Welcome to Transflower")
    return render(request, 'HelloApp/home/home.html')

def about(request):
    #return HttpResponse("Transflower Learning Pvt. Ltd.")
    return render(request, 'HelloApp/home/about.html')
   
def contact(request):
    #return render(request, 'HelloApp/home.html')
    #return HttpResponse("<p>601, Rama Apartment , Walwekar Nagar </p>")
    return render(request, 'HelloApp/home/contact.html')

def catalog(request):
    products = [
    {"name": "Laptop", "description": "A high-performance laptop", "price": 999.99},
    {"name": "Smartphone", "description": "A latest-generation smartphone", "price": 699.99},
    {"name": "Headphones", "description": "Noise-cancelling over-ear headphones", "price": 199.99},
    {"name": "Keyboard", "description": "Mechanical keyboard with RGB lighting", "price": 129.99},
    {"name": "Mouse", "description": "Wireless ergonomic mouse", "price": 49.99}
    ]
    return render(request, 'HelloApp/catalog/list.html',{'products': products})

def flowers(request):
    flowers = [
        Product("Gerbra", "Wedding Flower", 45.5),
        Product("Rose", "Valentine Flower", 65),
        Product("Jasmine","Smelling Flower", 23),
        Product("Lily", "Delicate Flower", 76),
        Product("Lotus", "worship", 12),
    ]
    return render(request, 'HelloApp/catalog/list.html',{'products': flowers})
    # return JsonResponse({'products': flowers})

def customers(request):

    customer=Customer("Sachin", "sachin.t@gmail.com", "988767654")

    customers = [
    Customer("Sachin", "sachin.t@gmail.com", "988767654"),
    Customer("Ravi", "sachin.t@gmail.com", "988767654"),
    Customer("Manish", "sachin.t@gmail.com", "988767654"),
    Customer("Sarang", "sachin.t@gmail.com", "988767654"),
    Customer("Seema", "sachin.t@gmail.com", "988767654"),
    ]

    return render(request, 'HelloApp/crm/customers.html',{'customers': customers})