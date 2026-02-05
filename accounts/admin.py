from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserChangeForm,UserCreationForm

# @admin.site.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    form = UserChangeForm
    add_form=UserCreationForm

    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)

admin.site.register(CustomUser,CustomUserAdmin)