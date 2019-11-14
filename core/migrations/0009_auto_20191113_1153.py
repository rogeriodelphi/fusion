# Generated by Django 2.2.5 on 2019-11-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191110_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-laptop-phone', 'Laptop'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Ícones'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=13, verbose_name='Ícone'),
        ),
    ]
