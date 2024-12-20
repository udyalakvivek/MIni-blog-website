# Generated by Django 5.1.3 on 2024-12-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blog_post_created_at_blog_post_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog_post",
            name="category",
            field=models.CharField(
                choices=[
                    ("general", "General"),
                    ("technology", "Technology"),
                    ("lifestyle", "Lifestyle"),
                    ("travel", "Travel"),
                    ("food", "Food"),
                    ("books", "Books"),
                ],
                default="general",
                max_length=70,
            ),
        ),
    ]