# Generated by Django 2.2.5 on 2019-10-09 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20191009_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sintom',
            name='consultapk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sintomlist', to='webapp.Consulta'),
        ),
    ]
