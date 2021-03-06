from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here

class User(AbstractUser):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username




class Field(models.Model):
    user = models.ForeignKey('User', related_name='fields', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название поля")
    description = models.TextField(blank=True, verbose_name="Описание")

    slug = models.SlugField(blank=True)
    available = models.BooleanField(default=True)
    create_date =models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    latitude = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    image = models.ImageField(upload_to='field/images')
    open_time = models.TimeField(null=True, blank=True, verbose_name="открытие")
    close_time = models.TimeField(null=True, blank=True, verbose_name="закрытие")
    shower = models.BooleanField(default=True, verbose_name="Душ")
    changing_room = models.BooleanField(default=True, verbose_name="Раздевалка")
    parking = models.BooleanField(default=True, verbose_name="Парковка")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('booking:field_view', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_date']



#
# titledef pre_save_field_slug(sender, instance, *args, **kwargs):
#     if not instance.slug
#         slug = slugify(translit(unicode(instance.name) reversed=True))
#         instance.slug = slug
#
# pre_save.connect(pre_save_field_slug, sender=Field)

class Image(models.Model):
    image = models.ImageField(upload_to='field/images')
    field = models.ForeignKey('Field', on_delete=models.CASCADE, related_name='images')

# class time-table(models.Model)
