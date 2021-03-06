# Generated by Django 2.2.5 on 2019-11-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191113_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Laptop'), ('lni-cog', 'Engrenagem')], max_length=16, verbose_name='Ícones'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Design'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem')], max_length=13, verbose_name='Ícone'),
        ),
    ]
