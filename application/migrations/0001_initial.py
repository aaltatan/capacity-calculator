# Generated by Django 5.1.3 on 2024-11-21 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Specialization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("is_specialist", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "degree",
                    models.CharField(
                        choices=[("Master", "Master"), ("Doctorate", "Doctorate")],
                        default="Doctorate",
                        max_length=100,
                    ),
                ),
                ("is_local", models.BooleanField(default=False)),
                (
                    "job_type",
                    models.CharField(
                        choices=[("Fulltime", "Fulltime"), ("Parttime", "Parttime")],
                        default="Fulltime",
                        max_length=100,
                    ),
                ),
                ("is_calculated", models.BooleanField(default=True)),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="application.faculty",
                    ),
                ),
                (
                    "specialization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="application.specialization",
                    ),
                ),
            ],
        ),
    ]
