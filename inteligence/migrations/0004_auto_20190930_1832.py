# Generated by Django 2.2.5 on 2019-09-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inteligence', '0003_auto_20190927_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isintom',
            name='measure',
        ),
        migrations.CreateModel(
            name='Ipotential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minlimit', models.IntegerField()),
                ('maxlimit', models.IntegerField()),
                ('potential', models.IntegerField()),
                ('isintompk', models.ForeignKey(on_delete=None, related_name='isintompk', to='inteligence.Isintom')),
            ],
        ),
    ]
