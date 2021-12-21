from django.shortcuts import render,redirect
from ClgApp.forms import RgForm,Userup,UsrgForm
from ClgApp.models import User
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def aboutus(request):
	return render(request,'html/about.html')

def register(request):
	y = User.objects.all()
	t = {}
	j = 0
	for i in y:
		if i.usrole == 1 or i.usrole == 3:
			t[j] = i.username,i.id
			j+=1
		else:
			continue
	if request.method == "POST":
		d = RgForm(request.POST)
		if d.is_valid():
			d.save()
			messages.success(request,"User Created Successfully")
			return redirect('/register')
	d = RgForm()
	return render(request,'html/register.html',{'g':d,'q':t.values()})

def usview(request,b):
	c = User.objects.get(id=b)
	return render(request,'html/userview.html',{'a':c})

def upd(request,t):
	n = User.objects.get(id=t)
	if request.method == "POST":
		g = Userup(request.POST,instance=n)
		if g.is_valid():
			g.save()
			messages.info(request,"user details Updated successfully")
			return redirect('/register')
	g = Userup(instance=n)
	return render(request,'html/uupdate.html',{'v':g})

def udl(request,m):
	p = User.objects.get(id=m)
	if request.method == "POST":
		p.delete()
		messages.warning(request,"user deleted Successfully")
		return redirect('/register')
	return render(request,'html/udel.html',{'v':p})

def regs(request):
	if request.method == "POST":
		r = UsrgForm(request.POST)
		if r.is_valid():
			r.save()
			return redirect('/lin')
	r = UsrgForm()
	return render(request,'html/rg.html',{'h':r})


