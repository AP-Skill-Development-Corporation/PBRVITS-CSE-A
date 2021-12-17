from django.urls import path
from ClgApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.aboutus,name="ab"),
	path('register/',views.register,name="rg"),
	path('uv/<int:b>/',views.usview,name="uvw"),
]