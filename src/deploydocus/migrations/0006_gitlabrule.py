# Generated by Django 5.0.2 on 2024-02-27 21:35

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deploydocus", "0005_alter_gitlabproject_merge_method"),
    ]

    operations = [
        migrations.CreateModel(
            name="GitlabRule",
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
                ("name", models.CharField(max_length=300)),
                (
                    "attribut",
                    models.CharField(
                        choices=[("merge_method", "Merge Method")], max_length=30
                    ),
                ),
            ],
            options={
                "verbose_name": "Rule",
                "verbose_name_plural": "Rules",
                "ordering": ["name"],
            },
        ),
    ]
