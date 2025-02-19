# Generated by Django 5.1 on 2024-09-11 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="organizador",
            name="email",
            field=models.EmailField(default="prueba@gmail.com", max_length=254),
        ),
        migrations.AlterField(
            model_name="evento",
            name="nombre",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="evento",
            name="organizador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventos",
                to="eventos.organizador",
            ),
        ),
    ]
