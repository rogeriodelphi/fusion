# Generated by Django 2.2.5 on 2019-11-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191105_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-users', 'Usuários'), ('lni-status-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-cog', 'Engrenagem')], max_length=13, verbose_name='Ícone'),
        ),
    ]
