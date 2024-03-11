from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class ShowRoomList(models.Model):
    name = models.CharField(max_length = 50)
    location  = models.CharField(max_length = 30)
    website = models.URLField(max_length = 100)

    def __str__(self):
        return self.name

class CarList(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    active = models.BooleanField(default = False)
    chassisnumber = models.CharField(max_length = 50,null=True)
    price = models.DecimalField(max_digits = 9, decimal_places = 2,null = True)
    showroom = models.ForeignKey(ShowRoomList,on_delete =models.CASCADE,related_name = 'Showrooms')

    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    apiuser = models.ForeignKey(User,on_delete = models.CASCADE)
    rating = models.IntegerField(validators =[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField(null = True)
    car = models.ForeignKey(CarList,on_delete =models.CASCADE,related_name = 'Car_Review')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.comment + " " + str(self.rating) + " " + self.created.strftime("%c")