# Generated by Django 4.1.2 on 2022-11-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0005_alter_property_street_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="dates",
            field=models.BigIntegerField(blank=True, null=True, verbose_name="dates"),
        ),
    ]
