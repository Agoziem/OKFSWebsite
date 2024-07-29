# Generated by Django 2.2 on 2024-07-29 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SRMS', '0016_auto_20240728_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualstudent',
            name='academicsession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SRMS.AcademicSession'),
        ),
        migrations.AlterField(
            model_name='annualresult',
            name='Student_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SRMS.AnnualStudent'),
        ),
    ]
