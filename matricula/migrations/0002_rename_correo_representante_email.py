# Generated by Django 4.2 on 2024-10-06 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matricula", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="representante",
            old_name="correo",
            new_name="email",
        ),
    ]
