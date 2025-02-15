# Generated by Django 4.2.6 on 2023-12-31 14:32

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a category name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=100)),
                ('email', models.EmailField(help_text='Enter your email', max_length=100)),
                ('message', models.TextField(help_text='Enter your message', max_length=100)),
                ('date_contacted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(blank=True, max_length=150, null=True)),
                ('main_description', ckeditor.fields.RichTextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('last_rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(help_text='Select categories for this post', to='core.category')),
            ],
            options={
                'verbose_name_plural': 'All projects',
                'ordering': ['date_posted'],
            },
        ),
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text='Select a rating')),
                ('post', models.ForeignKey(help_text='Select a post to review', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Enter your comment', max_length=300)),
                ('post', models.ForeignKey(help_text='Select a post to comment on', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
