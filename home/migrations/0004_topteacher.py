# Generated by Django 2.2 on 2023-11-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230416_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profileimage', models.ImageField(blank=True, upload_to='assets')),
                ('Profilename', models.CharField(blank=True, max_length=300)),
                ('Role', models.CharField(blank=True, max_length=300)),
                ('Phonenumber', models.CharField(blank=True, max_length=300)),
                ('Emailaddress', models.CharField(blank=True, max_length=300)),
                ('Facebookpage', models.CharField(blank=True, max_length=300)),
                ('Twitterpage', models.CharField(blank=True, max_length=300)),
                ('Whatsapp', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]