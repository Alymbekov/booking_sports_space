from django.contrib import admin
from booking.models import Field
from booking.models import Image



@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

