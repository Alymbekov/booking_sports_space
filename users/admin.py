from django.contrib import admin
from authtools.admin import UserAdmin
from authtools.forms import AdminUserChangeForm
from .models import User, Customer, SportSpaceAdmin


class CustomAdminUserChangeForm(AdminUserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Raw passwords are not stored, so there is no way to see this"
            " user's password, but you can change the password using"
            " <a href=\"../password/\">this form</a>.")


class MyUserAdmin(UserAdmin):
    form = CustomAdminUserChangeForm
    fieldsets = (("User info", {"fields": ("full_name",)}),) + UserAdmin.fieldsets
    list_display = ("email", "full_name", "is_superuser")
    search_fields = ["email", "full_name"]

admin.site.register(User, MyUserAdmin)
admin.site.register(Customer)
admin.site.register(SportSpaceAdmin)
