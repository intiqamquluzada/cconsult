# Generated by Django 4.2.7 on 2023-11-18 17:41

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0016_emails_location_phones'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(upload_to=services.uploader.Uploader.upload_photo_to_logo)),
                ('logo_name', models.CharField(max_length=255, verbose_name='right side of logo')),
                ('emails', models.ManyToManyField(to='my_app.emails', verbose_name='Emails')),
                ('locations', models.ManyToManyField(to='my_app.location', verbose_name='locations')),
                ('phones', models.ManyToManyField(to='my_app.phones', verbose_name='phones')),
            ],
            options={
                'verbose_name': 'main information',
                'verbose_name_plural': 'main informations',
                'ordering': ('-created_at',),
            },
        ),
    ]
