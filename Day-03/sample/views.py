from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
	return HttpResponse("<h1 style='color:green'>hello world</h1>")

def state(request,y):
	return HttpResponse("Hi Welcome {}".format(y))

def frt(self,p,t):
	return HttpResponse("<!Doctype=html><html><head><title>Demo</title></head><body><h2>Entered name is: {} and number is: {}</h2></body></html>".format(t,p))

def stdnt(request,rl,na,yr):
	h = {'roll':rl,'name':na,'year':yr}
	return render(request,'html/sample.html',h)

def empdetails(request,eid,ename,desg,sal):
	t = {'e':eid,'en':ename,'d':desg,'s':sal}
	return render(request,'html/employee.html',t)

def jvt(request,name):
	return HttpResponse("<script>alert('Hi welcome {}')</script>".format(name))

def wtg(request,et):
	return render(request,'html/jst.html',{'u':et})

def dynt(request):
	return render(request,'html/stform.html')

def bts(request):
	if request.method == "POST":
		roll = request.POST['rn']
		sname = request.POST['sn']
		yer = request.POST['yr']
		print(roll,sname,yer)
		return render(request,'html/display.html',{'r':roll,'sn':sname,'yr':yer})
	return render(request,'html/bt.html')













