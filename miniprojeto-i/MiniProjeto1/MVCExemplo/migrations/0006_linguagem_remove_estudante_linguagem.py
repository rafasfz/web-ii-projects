# Generated by Django 4.1.1 on 2022-09-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVCExemplo', '0005_auto_20220917_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='linguagem',
        ),
    ]