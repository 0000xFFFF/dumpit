# Generated by Django 5.1.1 on 2024-09-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Picture",
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
                ("filename", models.CharField(max_length=255)),
                ("metadata", models.CharField(max_length=255)),
                ("width", models.IntegerField()),
                ("height", models.IntegerField()),
                ("size_in_bytes", models.IntegerField()),
            ],
        ),
    ]
