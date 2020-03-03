# Generated by Django 2.2.5 on 2019-09-27 18:43

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sintom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('measure', jsonfield.fields.JSONField()),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('parent', models.ForeignKey(on_delete=None, related_name='parent_zone', to='inteligence.Zone')),
            ],
        ),
    ]
