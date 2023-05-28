# Generated by Django 4.2.1 on 2023-05-28 16:04

from django.db import migrations, models
import samolet.models


class Migration(migrations.Migration):

    dependencies = [
        ("samolet", "0011_rename_flat_check_flat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="checks/",
                validators=[samolet.models.validate_file_size],
            ),
        ),
    ]
