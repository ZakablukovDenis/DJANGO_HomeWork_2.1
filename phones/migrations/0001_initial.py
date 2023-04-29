# Generated by Django 4.2 on 2023-04-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Наименование')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('lte_exists', models.BooleanField(default=False, verbose_name='LTE')),
                ('slug', models.SlugField(default='', verbose_name='URL')),
            ],
        ),
    ]
