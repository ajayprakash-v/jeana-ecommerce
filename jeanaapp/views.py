from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
	product=Cart.objects.filter(user_id=request.user.id)
	return render(request,'home.html',{'product':product})

def tshirt(request):
	menu=''
	if request.method=='GET':
		menu=request.GET['menu']
	print(menu)
	if menu=='all':
		product=Product.objects.all()
	else:
		product=Product.objects.filter(category=menu)
	ser=serializers.serialize('json',product)	
	return JsonResponse(ser,safe=False)

def showproduct(request):
	if request.method=='GET':
		idd=request.GET['id']
		product=Product.objects.filter(id=idd)
		variantm=Variant.objects.filter(product_id=idd,size_id=2)
		variantl=Variant.objects.filter(product_id=idd,size_id=3)
		print(variantl)
		ser1=serializers.serialize('json',product)
		vs=serializers.serialize('json',variantm)
		vl=serializers.serialize('json',variantl)
	return JsonResponse([ser1,vs,vl],safe=False)

def register(request):
	if request.method=='GET':
		name=request.GET['name']
		email=request.GET['email']
		password=request.GET['pass']
		user=User()
		user.username=name
		user.email=email
		user.set_password(password)
		user.save()
	return HttpResponse('done')

def loginn(request):
	status='error'
	if request.method=='GET':
		namee=request.GET['lname']
		password=request.GET['lpass']
		user=authenticate(username=namee,password=password)
		if user:
			status='done'
			login(request,user)
	return HttpResponse(status)

def onlinecheck(request):
	online='off'
	if request.user.is_active:
		online='on'
	return HttpResponse(online)

def logt(request):
	logout(request)
	return HttpResponse('done')

def cart(request):
	if request.method=='GET':
		idd=request.GET['idd']
		qu=request.GET['quantity']
		to=request.GET['total']
		obj=Cart()
		obj.product_id=idd
		obj.quantity=qu
		obj.totalprice=to
		obj.user=request.user
		obj.save()
		product=Product.objects.filter(id=idd)
		ser=serializers.serialize('json',product)
	return JsonResponse(ser,safe=False)

def delt(request):
	if request.method=='GET':
		idd=request.GET['id']
		user=request.user.id
		Cart.objects.filter(user_id=user,id=idd).delete()
	return HttpResponse('done')