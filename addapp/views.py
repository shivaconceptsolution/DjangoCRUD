from django.shortcuts import render
from django.http import HttpResponse
from . models import Register
def reg(request):
	return render(request,"addapp/reg.html")
def reglogic(request):
	obj = Register(emailid=request.POST["txtemail"],password=request.POST["txtpass"],mobile=request.POST["txtmobile"],fullname=request.POST["txtname"])
	obj.save()
	return render(request,"addapp/reg.html",{'msg':'registration successfully'})
def viewreg(request):
	res = Register.objects.all()
	return render(request,"addapp/viewreg.html",{'res1':res})
def index(request):
	return render(request,"addapp/index.html")
def addlogic(request):
	course   = request.POST.getlist('course[]')	 
	some_var = request.POST.getlist('checks[]')
	data1=''
	for data2 in course:
	    data1=data1+data2 +" "
	data=''
	for data3 in som_var:
	    data=data+data3 +" "	
	return HttpResponse("data is "+(data1+data))