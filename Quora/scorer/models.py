from django.db import models

class Customer(models.Model):
    #id = models.Field(primary_key = True)
    mail = models.EmailField(default='teacher@teacher.com',unique=True)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    profile = models.URLField()
    def __str__(self): 
         return self.fName+" "+self.lName

class Articles(models.Model):
	title = models.CharField(max_length=350)
	body = models.CharField(max_length=12000)
	image = models.URLField()
	def __str__(self): 
         return self.title