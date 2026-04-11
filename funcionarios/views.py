from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def home(request):
    return HttpResponse("<h1>Home Pública</h1><p>Bem-vindo à empresa! Esta página é aberta a todos.</p>")

class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionarios/painel.html'