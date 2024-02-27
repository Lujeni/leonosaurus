# Generated by Django 5.0.2 on 2024-02-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deploydocus", "0008_alter_gitlabrule_options_gitlabrule_expected"),
    ]

    operations = [
        migrations.AlterField(
            model_name="policy",
            name="gitlab_rules",
            field=models.ManyToManyField(blank=True, to="deploydocus.gitlabrule"),
        ),
        migrations.AlterField(
            model_name="policy",
            name="rules",
            field=models.ManyToManyField(blank=True, to="deploydocus.rule"),
        ),
    ]
