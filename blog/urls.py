from django.urls import path
from . import views


urlpatterns = [
    path('',views.posts),
    path('<name_post>/',views.about)
]