# Generated by Django 3.1.4 on 2020-12-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='DisplayResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='gallery')),
            ],
        ),
    ]
