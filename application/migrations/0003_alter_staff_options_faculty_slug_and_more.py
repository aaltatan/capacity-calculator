# Generated by Django 5.1.3 on 2024-11-23 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0002_alter_faculty_options_faculty_students_count_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="staff",
            options={
                "ordering": (
                    "faculty__name",
                    "is_calculated",
                    "job_type",
                    "-specialization__is_specialist",
                    "is_local",
                    "degree",
                ),
                "verbose_name": "Staff",
                "verbose_name_plural": "Staff",
            },
        ),
        migrations.AddField(
            model_name="faculty",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="specialization",
            name="faculties",
            field=models.ManyToManyField(
                related_name="specializations", to="application.faculty"
            ),
        ),
        migrations.AddField(
            model_name="specialization",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="staff",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="faculty",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="specialization",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="staff",
            name="faculty",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff",
                to="application.faculty",
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="staff",
            name="specialization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff",
                to="application.specialization",
            ),
        ),
    ]
