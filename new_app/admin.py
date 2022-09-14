from django.contrib import admin
from .models import Book, Publisher

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']

# admin.site.register(Book)
admin.site.register(Publisher)
