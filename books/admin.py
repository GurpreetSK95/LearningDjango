from django.contrib import admin
from .models import Book, Publisher, Author

# tell django to offer interface for these models
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)