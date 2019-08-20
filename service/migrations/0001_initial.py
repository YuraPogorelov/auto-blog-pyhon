# Generated by Django 2.2.4 on 2019-08-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=120, verbose_name='URL')),
                ('text', models.TextField(verbose_name='Текст категории')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Баннер')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.CharField(max_length=120, verbose_name='Description')),
                ('keywords', models.CharField(max_length=250, verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
