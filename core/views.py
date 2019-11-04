from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'Index.html'


class TesteView(TemplateView):
    template_name = '500.html'