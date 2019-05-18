from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here

class Field(models.Model):
    user = models.ForeignKey('user.User', related_name='fields', on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, verbose_name="Описание")

    slug = models.SlugField(blank=True)
    available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=19, decimal_places=10,null=True, blank=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)

    def __str__(self):
        return self.title
#
# titledef pre_save_field_slug(sender, instance, *args, **kwargs):
#     if not instance.slug
#         slug = slugify(translit(unicode(instance.name) reversed=True))
#         instance.slug = slug
#
# pre_save.connect(pre_save_field_slug, sender=Field)

class Image(models.Model):
    image = models.ImageField(upload_to='field/images')
    field = models.ForeignKey('Field', on_delete = models.CASCADE, related_name='images')







#class time-table(models.Model)


