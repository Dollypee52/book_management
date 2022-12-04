from django.contrib import admin
from .models import Book, Publisher, User
from django.contrib.auth.admin import  UserAdmin as AdminUser


# Register your models here.

@admin.register(User)
class UserAdmin(AdminUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email","username", "password1", "password2","first_name","last_name"),
            },
        ),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']


# admin.site.register(Book)
admin.site.register(Publisher)
