# Generated by Django 4.2.7 on 2023-11-17 15:26

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_to_slider, verbose_name='slider image')),
            ],
            options={
                'verbose_name': 'Home slider',
                'verbose_name_plural': 'Home sliders',
                'ordering': ('-created_at',),
            },
        ),
    ]
