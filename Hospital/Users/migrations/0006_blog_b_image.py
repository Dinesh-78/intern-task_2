# Generated by Django 5.0 on 2024-01-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_rename_body_blog_content_remove_blog_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='b_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]