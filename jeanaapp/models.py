from django.db import models
from django.contrib.auth.models import User 

class Size(models.Model):
	size=models.CharField(max_length=20,default='')
	def __str__(self):
		return str(self.size)

class Product(models.Model):
	cat=(('ts','t-shirt'),('hoo','hoodies'),('sp','sportswear'),('sh','shoes'),('bg','bags'))
	gen=(('M','Male'),('F','Female'),('B','Both'))
	name=models.CharField(max_length=100,default='')
	discription=models.CharField(max_length=500,default='')
	image=models.ImageField(upload_to='images/',blank='true')
	category=models.CharField(max_length=10,choices=cat,default='newin')
	gender=models.CharField(max_length=10,choices=gen,blank=True)
	baseprice=models.IntegerField(default=0)
	quantity=models.IntegerField(default=0)

	def __str__(self):
		return str(self.name)

class Variant(models.Model):
	product=models.ForeignKey(Product,blank=False,on_delete=models.CASCADE)
	size=models.ForeignKey(Size,blank=True,on_delete=models.CASCADE)
	price=models.IntegerField(default=0)
	image=models.ImageField(upload_to='images/',blank='true')
	
	def __str__(self):
		return str(self.product)

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=1)
	totalprice=models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.user)