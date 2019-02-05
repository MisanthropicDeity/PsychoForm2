from django.db import models
from django.core.validators import MaxValueValidator

class submission(models.Model):
    usrname = models.CharField(max_length = 140)
    email = models.CharField(max_length = 140)
    age = models.PositiveIntegerField(validators =[MaxValueValidator(70)], default=0)
    gender = models.CharField(max_length = 10)
    quest1 = models.CharField(max_length = 40, default = "")
    quest2 = models.CharField(max_length = 40, default = "")
    quest3 = models.CharField(max_length = 40, default = "")
    quest4 = models.CharField(max_length = 40, default = "")
    quest5 = models.CharField(max_length = 40, default = "")
    quest6 = models.CharField(max_length = 40, default = "")
    quest7 = models.CharField(max_length = 40, default = "")
    quest8 = models.CharField(max_length = 40, default = "")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    #time = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.usrname
    
class feedback(models.Model):
    feed = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    #time = models.DateTimeField(default=datetime.now, blank=True)