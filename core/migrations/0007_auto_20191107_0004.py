# Generated by Django 2.2.5 on 2019-11-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191105_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Laptop'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile')], max_length=16, verbose_name='Ícones'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-cog', 'Engrenagem'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile')], max_length=13, verbose_name='Ícone'),
        ),
    ]