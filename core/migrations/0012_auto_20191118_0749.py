# Generated by Django 2.2.5 on 2019-11-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191118_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='bio',
            field=models.TextField(max_length=400, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='descricao',
            field=models.TextField(max_length=400, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Laptop'), ('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile'), ('lni-users', 'Usuários'), ('lni-leaf', 'Folha')], max_length=16, verbose_name='Ícones'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='recurso',
            field=models.CharField(max_length=150, verbose_name='Recurso'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=400, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Gráfico')], max_length=13, verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='servico',
            field=models.CharField(max_length=150, verbose_name='Serviço'),
        ),
    ]
