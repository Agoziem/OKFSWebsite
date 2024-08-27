# Generated by Django 2.2 on 2024-08-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='carousel_images/')),
                ('animation_title', models.CharField(default='fadeInRight', max_length=50)),
                ('animation_tag', models.CharField(default='fadeInLeft', max_length=50)),
                ('animation_cta', models.CharField(default='fadeInBottomLeft', max_length=50)),
                ('cta_link', models.CharField(default='#', max_length=255)),
                ('cta_text', models.CharField(default='Register now', max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
