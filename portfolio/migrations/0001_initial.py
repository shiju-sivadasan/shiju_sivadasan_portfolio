# Generated by Django 5.1.3 on 2024-11-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=255)),
                ('b_desc', models.TextField()),
                ('b_link', models.CharField(max_length=255)),
                ('b_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('point_1', models.CharField(max_length=100)),
                ('point_2', models.CharField(max_length=100)),
                ('point_3', models.CharField(max_length=100)),
                ('point_4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_desc', models.TextField()),
                ('p_link', models.CharField(max_length=255)),
                ('p_image', models.ImageField(upload_to='project_images/')),
            ],
        ),
    ]
