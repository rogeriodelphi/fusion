from django.views.generic import TemplateView

from .models import Servico, Funcionario, Recurso

class IndexView(TemplateView):
    template_name = 'Index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = list(Recurso.objects.order_by('?').all())
        context['meialista'] = int(len(context['recursos']))
        print (f"Testando:{type(context['recursos'])}")
        return context





class TesteView(TemplateView):
    template_name = '500.html'

