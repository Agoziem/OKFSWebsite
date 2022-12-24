# Generated by Django 2.2 on 2022-12-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRMS', '0003_annualresult_annualstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students_Pin_and_ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(blank=True, max_length=100)),
                ('student_name', models.CharField(blank=True, default='No name', max_length=100)),
                ('student_id', models.CharField(blank=True, max_length=100, null=True)),
                ('student_pin', models.BigIntegerField(blank=True, null=True)),
                ('student_class', models.CharField(blank=True, default='No class', max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Pin',
        ),
    ]