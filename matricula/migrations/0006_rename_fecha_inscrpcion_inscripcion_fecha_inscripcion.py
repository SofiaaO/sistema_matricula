# Generated by Django 4.2 on 2024-10-06 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matricula", "0005_alter_programa_agrupacion"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inscripcion",
            old_name="fecha_inscrpcion",
            new_name="fecha_inscripcion",
        ),
    ]
