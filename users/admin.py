from django.contrib import admin
from .models import Users

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "is_active", "is_staff")
    search_fields = ["first_name", "last_name", "username", "email"]

    class Media:
        js = ("js/admin.js", )
        css = {
            'all': ('css/admin.css', )
        }
