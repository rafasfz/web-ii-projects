# Generated by Django 4.1.1 on 2022-09-24 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MVCAppData', '0005_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=512, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=512, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Disciplina'),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasy_name', models.CharField(max_length=512, verbose_name='Nome Fantasia')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MVCAppData.student', verbose_name='Estudante')),
            ],
        ),
    ]
