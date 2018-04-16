from django.shortcuts import render
from . import views
# Create your views here.
urlpatterns = [
    url(r'^$', views.pot_list),
]
