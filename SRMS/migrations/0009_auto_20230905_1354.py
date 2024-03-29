# Generated by Django 2.2 on 2023-09-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRMS', '0008_auto_20230416_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='newsletter',
            new_name='newsletterConstruct',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='Term',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='newsletterFile',
            field=models.FileField(blank=True, upload_to='media/Newsletter'),
        ),
    ]
