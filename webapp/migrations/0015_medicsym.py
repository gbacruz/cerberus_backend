# Generated by Django 2.2.2 on 2020-03-11 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20200304_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicSym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(default='dolor', max_length=500, verbose_name='sym')),
                ('level', models.IntegerField(default=20)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Medic')),
            ],
        ),
    ]
