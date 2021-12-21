from django.urls import path
from ClgApp import views
from django.contrib.auth import views as av
urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.aboutus,name="ab"),
	path('register/',views.register,name="rg"),
	path('uv/<int:b>/',views.usview,name="uvw"),
	path('up/<int:t>/',views.upd,name="up"),
	path('ud/<int:m>/',views.udl,name="dl"),
	path('lin/',av.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lon/',av.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path('reg/',views.regs,name="rgs"),
]