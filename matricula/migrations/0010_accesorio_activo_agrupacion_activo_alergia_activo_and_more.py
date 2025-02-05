# Generated by Django 4.2 on 2024-11-05 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matricula", "0009_alter_alumno_cedula"),
    ]

    operations = [
        migrations.AddField(
            model_name="accesorio",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="agrupacion",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="alergia",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="alumno",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="becado",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="catedra",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="categoriainstrumento",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="color",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="condicionespecial",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="inscripcion",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="instrumento",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="marcainstrumento",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="medicamento",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="modeloinstrumento",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="nivelestudiantil",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="nivelts",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="programa",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="quienretira",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="representante",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="tipobeca",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="tipocatedra",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="tratamiento",
            name="activo",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="turno",
            name="activo",
            field=models.BooleanField(default=True),
        ),
    ]
