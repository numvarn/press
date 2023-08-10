# Generated by Django 4.2.4 on 2023-08-10 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="news.author"
            ),
        ),
    ]
