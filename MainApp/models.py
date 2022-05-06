from django.db import models
from django.forms import CharField
from django.utils.timezone import now

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza =  models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name =  models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza =  models.ForeignKey(Pizza, on_delete=models.CASCADE)
    commentor_name = CharField(max_length=50)
    comment_text = CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text



