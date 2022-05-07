from django.shortcuts import render, redirect

from .forms import CommentForm
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
    toppings = pizza.topping_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'MainApp/pizza.html', context)

# def new_comment(request):
#     if request.method != 'POST':
#         form = CommentForm()
#     else:
#         form = CommentForm(data=request.POST)

#         if form.is_valid():
#             new_comment = form.save()

#             return redirect('MainApp:comment')
#     context = {'form':form}
#     return render(request, 'MainApp/new_comment.html', context)

