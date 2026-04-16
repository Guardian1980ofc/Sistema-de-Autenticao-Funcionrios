from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Employee, Order

def home(request):
    return HttpResponse("<h1>Home Pública</h1><p>Bem-vindo à empresa! Esta página é aberta a todos.</p>")
#motivo FBV:
#simplicidade: evitar criação de arquivo html para uma pagina que não tem fluxo de dados

class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionarios/painel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['funcionarios'] = Employee.objects.filter(is_deleted=False)
        context['pedidos'] = Order.objects.filter(is_deleted=False)
        return context
    
