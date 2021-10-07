from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class Web3LoginView(TemplateView):
    template_name = "pages/web3-login.html"
