from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:number_post>/',views.about_by_num),
    path('<str:name_post>/',views.about),
]