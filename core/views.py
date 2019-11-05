from django.views.generic import TemplateView

from .models import Servico, Funcionario

class IndexView(TemplateView):
    template_name = 'Index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context





class TesteView(TemplateView):
    template_name = '500.html'

