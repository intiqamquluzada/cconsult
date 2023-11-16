# Generated by Django 4.2.7 on 2023-11-15 18:13

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_aboutmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSideBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title_1', models.CharField(max_length=255, verbose_name='Title 1')),
                ('desc_1', models.TextField(verbose_name='Description 1')),
                ('image_1', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_to_about)),
                ('title_2', models.CharField(max_length=255, verbose_name='Title 2')),
                ('desc_2', models.TextField(verbose_name='Description 2')),
                ('image_2', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_to_about)),
                ('title_3', models.CharField(max_length=255, verbose_name='Title 3')),
                ('desc_3', models.TextField(verbose_name='Description 3')),
                ('image_3', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_to_about)),
            ],
            options={
                'verbose_name': 'About Side bar',
                'verbose_name_plural': 'About Side Bar',
                'ordering': ('-created_at',),
            },
        ),
    ]
