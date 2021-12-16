from django.urls import path
from ClgApp import views

urlpatterns = [
	path('',views.home,name="hm"),
]