# Generated by Django 4.1.2 on 2022-10-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0003_alter_project_company_alter_project_dates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="price",
            field=models.BigIntegerField(verbose_name="price"),
        ),
    ]
