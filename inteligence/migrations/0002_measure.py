# Generated by Django 2.2.5 on 2019-09-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inteligence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('sintom', models.ForeignKey(on_delete=None, related_name='sintom_measure', to='inteligence.Sintom')),
            ],
        ),
    ]
