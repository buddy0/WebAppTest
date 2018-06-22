from django.urls import path
from . import views

urlpatterns = [
  path('',views.func1,name='func1'),
  #path('1/',views.func1,name='func1'),
  #path('2/',views.func2,name='func2'),
 ]

