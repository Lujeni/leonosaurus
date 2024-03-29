# Generated by Django 5.0.2 on 2024-02-21 20:44

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deploydocus", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GitlabProject",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("path_with_namespace", models.CharField(max_length=3000)),
            ],
            options={
                "verbose_name": "Gitlab project",
                "verbose_name_plural": "Gitlab projects",
                "ordering": ["path_with_namespace"],
            },
        ),
    ]
