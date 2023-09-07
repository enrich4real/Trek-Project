from django.urls import path, include
from .views import LoginView, LogoutView,HomeView

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(),name='home'),
]