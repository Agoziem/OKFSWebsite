# Generated by Django 2.2 on 2022-04-14 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elibrary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='date_published',
            new_name='date_uploaded',
        ),
        migrations.RemoveField(
            model_name='ebook',
            name='Ebook',
        ),
        migrations.AddField(
            model_name='ebook',
            name='Ebooklink',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='Ebookimage',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
