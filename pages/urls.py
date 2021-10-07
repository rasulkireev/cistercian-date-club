from django.urls import path

from .views import HomeView, Web3LoginView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("web3-login", Web3LoginView.as_view(), name="web3-login"),
]
