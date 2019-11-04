from django.db import models

from stdimage.models import StdImageField


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = {
        ('Ini_cog', 'Engrenagem'),
        ('Ini_status-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('Ini-layers', 'Design'),
        ('Ini-mobile', 'Mobile'),
        ('Ini-rocket', 'Foguete'),
    }
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name: 'Serviço'
        verbose_name_plural: 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'tumb': {'with':480, 'height':480, 'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twiter = models.CharField('Twiter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome