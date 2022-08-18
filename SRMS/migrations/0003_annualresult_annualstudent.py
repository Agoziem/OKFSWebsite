# Generated by Django 2.2 on 2022-07-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRMS', '0002_assignments'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(blank=True, max_length=100)),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=100)),
                ('Subject', models.CharField(blank=True, max_length=100)),
                ('FirstTerm', models.CharField(blank=True, max_length=100)),
                ('SecondTerm', models.CharField(blank=True, max_length=100)),
                ('ThirdTerm', models.CharField(blank=True, max_length=100)),
                ('Total', models.CharField(blank=True, max_length=100)),
                ('Average', models.CharField(blank=True, max_length=100)),
                ('Grade', models.CharField(blank=True, max_length=100)),
                ('SubjectPosition', models.CharField(blank=True, max_length=100)),
                ('Remark', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AnnualStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=100)),
                ('TotalScore', models.CharField(blank=True, max_length=100)),
                ('Totalnumber', models.CharField(blank=True, max_length=100)),
                ('Average', models.CharField(blank=True, max_length=100)),
                ('Position', models.CharField(blank=True, max_length=100)),
                ('Term', models.CharField(blank=True, max_length=100)),
                ('Academicsession', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]