from django.urls import path

from . import views

app_name = 'trek_page'
urlpatterns = [
    #Home Page
    path('', views.index, name = 'index'),
    path('index/',  views.IndexView.as_view(), name = 'index'),
]
