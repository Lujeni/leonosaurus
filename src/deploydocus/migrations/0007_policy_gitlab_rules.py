# Generated by Django 5.0.2 on 2024-02-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deploydocus", "0006_gitlabrule"),
    ]

    operations = [
        migrations.AddField(
            model_name="policy",
            name="gitlab_rules",
            field=models.ManyToManyField(to="deploydocus.gitlabrule"),
        ),
    ]
