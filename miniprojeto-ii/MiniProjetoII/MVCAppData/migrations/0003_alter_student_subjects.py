# Generated by Django 4.1.1 on 2022-09-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVCAppData', '0002_alter_course_description_alter_student_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(null=True, to='MVCAppData.subject', verbose_name='Disciplinas'),
        ),
    ]
