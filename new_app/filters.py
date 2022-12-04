from django_filters import FilterSet


from new_app.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'isbn': ['exact', 'contains'],
            'date_published': ['isnull', 'year__gt'],
            'price': ['gt', 'lt']
        }