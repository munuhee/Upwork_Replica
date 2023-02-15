# Generated by Django 4.1.5 on 2023-02-12 13:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to='project_pics'),
            preserve_default=False,
        ),
    ]