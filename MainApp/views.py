from django.shortcuts import render

from MainApp.models import Pizza, Topping, Comment

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}

    return render(request,'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    comments = pizza.entry_set.order_by('date_added')
    context = {'pizza':pizza, 'comments':comments}

    return render(request, 'MainApp/pizza.html', context)


