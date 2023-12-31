# Generated by Django 4.2.5 on 2023-11-13 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='ad')),
                ('position', models.CharField(max_length=255, verbose_name='vezifesi')),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_to_team)),
            ],
            options={
                'verbose_name': 'comanda',
                'verbose_name_plural': 'comanda',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('title',), 'verbose_name': 'bloq', 'verbose_name_plural': 'bloqlar'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('name',), 'verbose_name': 'contact', 'verbose_name_plural': 'contactlar'},
        ),
        migrations.AlterModelOptions(
            name='quota',
            options={'ordering': ('name',), 'verbose_name': 'quota', 'verbose_name_plural': 'quotalar'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('title',), 'verbose_name': 'xidet adi', 'verbose_name_plural': 'xidmet adlari'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_to_blog),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_to_service),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('description', models.TextField(verbose_name='metn')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'istifadeci reyi',
                'verbose_name_plural': 'istifadeci reyleri',
                'ordering': ('-created_at',),
            },
        ),
    ]
