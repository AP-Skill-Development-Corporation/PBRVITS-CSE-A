from django.shortcuts import render
from ClgApp.forms import RgForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def aboutus(request):
	return render(request,'html/about.html')

def register(request):
	y = User.objects.all() 
	if request.method == "POST":
		d = RgForm(request.POST)
		if d.is_valid():
			d.save()
	d = RgForm()
	return render(request,'html/register.html',{'g':d,'q':y})

def usview(request,b):
	c = User.objects.get(id=b)
	return render(request,'html/userview.html',{'a':c})

