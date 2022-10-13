# Generated by Django 4.1.1 on 2022-09-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaOperacional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiroNome', models.CharField(max_length=50)),
                ('ultimoNome', models.CharField(max_length=50)),
                ('curso', models.CharField(max_length=50)),
                ('linguagem', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('sistemasOperacionais', models.ManyToManyField(to='MVCExemplo.sistemaoperacional')),
            ],
        ),
    ]
