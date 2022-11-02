from email.policy import default
from statistics import mode
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}' 

class Portfolio(models.Model):
    
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.title}'

class Summary(models.Model):
    
    summary_title = models.TextField(default=True)

    def __str__(self):
        return f'{self.summary_title}'

class PageText(models.Model):
    
    title = models.TextField()
    last_title = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
class Welcome(models.Model):
    
    first_title = models.TextField()
    second_title = models.TextField()

    def __str__(self):
        return f'{self.first_title}'

class Skils(models.Model):
    
    image_icon = models.ImageField(upload_to='img/')
    url_icon = models.TextField(default=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}' 
 
class Contact(models.Model):
   
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField()
    number = models.IntegerField(default=True)

    def __str__(self):
        return f'{self.name}' 
    
class Animation(models.Model):
    
    animation = models.ImageField(upload_to='img/')
    url_animation = models.TextField(default=True)

    def __str__(self):
        return f'{self.animation}' 

class Photo(models.Model):
    
    image = models.ImageField(upload_to='img/')
    url_image = models.TextField(default=True)

    def __str__(self):
        return f'{self.image}'