from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=75, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(default=False, verbose_name='LTE')
    slug = models.SlugField(default="", null=False, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.release_date}'
