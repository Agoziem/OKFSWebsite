# Generated by Django 2.2 on 2024-07-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRMS', '0017_auto_20240729_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualstudent',
            name='Remark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='annualstudent',
            name='Verdict',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
