# Generated by Django 2.2.2 on 2020-03-12 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20200312_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediagnostic',
            name='special',
        ),
        migrations.AddField(
            model_name='prediagnostic',
            name='special',
            field=models.ManyToManyField(to='webapp.Specialist'),
        ),
    ]