# Generated by Django 3.1.4 on 2020-12-13 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20201213_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinedose',
            name='vaccine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.vaccinemanufacturer'),
        ),
    ]
