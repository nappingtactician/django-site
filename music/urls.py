from django.contrib import admin
from django.conf.urls import url
from django.urls import include,path
from . import views
app_name='music'

urlpatterns = [

    path('', views.index, name = 'index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^([0-9]+)/favorite/$', views.favorite, name = 'favorite'),

]
