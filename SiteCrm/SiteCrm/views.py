from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"

class LoginPage(TemplateView):
    template_name = "login.html"