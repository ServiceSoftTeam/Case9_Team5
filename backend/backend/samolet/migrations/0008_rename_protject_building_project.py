# Generated by Django 4.2.1 on 2023-05-28 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("samolet", "0007_remove_flat_building"),
    ]

    operations = [
        migrations.RenameField(
            model_name="building",
            old_name="protject",
            new_name="project",
        ),
    ]
