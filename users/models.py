from django.conf import settings
from authtools.models import AbstractEmailUser
from django.db import models

class User(AbstractEmailUser):
    full_name = models.CharField('full_name', max_length=255, blank=True)
    is_company = models.BooleanField(default=False)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return '{name} < {email}>'.format(
            name=self.full_name,
            email=self.email,
        )


def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)



class Customer(models.Model):
    default_profile_image = 'profile.jpg'
    photo = models.ImageField(
        default = default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer'
    )

    def __str__(self):
        return "{} профиль клиента".format(self.user.email)


class SportSpaceAdmin(models.Model):
    default_profile_image = 'profile.jpg'
    photo = models.ImageField(
        default = default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sportadmin'
    )

    def __str__(self):
        return "{} владелец поля".format(self.user.email)
