from django.urls import path
from . import views
urlpatterns = [
  path('reg',views.reg,name='reg'),
  path('reglogic',views.reglogic,name='reglogic'),
  path('viewreg',views.viewreg,name='viewreg'),
  path('',views.index,name='index'),
  path('/addlogic',views.addlogic,name='addlogic')

]