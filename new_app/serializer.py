from rest_framework import serializers

# class BookSerializer(serializers.Serializer): # noqa
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)
#     date_published = serializers.DateField()
#     isbn = serializers.CharField(max_length=20)
#     price = serializers.DecimalField(max_digits=8, decimal_places=2)
from new_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['title', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255, source='title')
    # publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # book_title = serializers.CharField(max_length=255, source='title')
    # publisher = PublisherSerializer()
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='new_app:publisher_detail'
    # )

    class Meta:
        model = Book
        # fields = "__all__",
        fields = ['title', 'description', 'isbn', 'price', 'publisher']
        # fields = ['book_title', 'description', 'isbn', 'price','publisher']
        # exclude = ['genre', ]
