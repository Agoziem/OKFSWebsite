# Generated by Django 2.2 on 2023-11-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0002_auto_20231124_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Role',
            field=models.CharField(blank=True, choices=[('Teacher', 'Teacher'), ('Formteacher', 'Formteacher')], default='Teacher', max_length=200),
        ),
    ]