# Generated by Django 2.2.5 on 2019-11-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-stats-up', 'Gráfico'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete')], max_length=13, verbose_name='Ícones'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='recurso',
            field=models.CharField(max_length=100, verbose_name='Recurso'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-stats-up', 'Gráfico'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete')], max_length=13, verbose_name='Ícone'),
        ),
    ]
