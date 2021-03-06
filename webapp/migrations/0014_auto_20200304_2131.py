# Generated by Django 2.2 on 2020-03-04 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0013_auto_20200303_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='hipotesis',
            new_name='patient',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='paciente',
        ),
        migrations.AddField(
            model_name='consulta',
            name='userapply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pacientepk', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
