from django.contrib import admin
from .models import Book, Publisher, Author


# custom class to show following author related columns in table on website
# provides search capabilities
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('title',)  # list ka syaapa, needs a , at end
    date_hierarchy = 'publication_date'  # date filter
    ordering = ('-publication_date',)

    # It's recommend using filter_horizontal for any ManyToManyField that has more than 10 items
    filter_horizontal = ('author',)     # run http://127.0.0.1:8000/admin/books/book/add/ to see difference

    #  there’s a magnifying-glass icon that you can click to pull up a pop-up window,
    # from which you can select the publisher to add
    raw_id_fields = ('publisher',)    # changes from select to text field (used for foreign key)


# tell django to offer interface for these models
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)  # Register the Author model with the AuthorAdmin options
admin.site.register(Publisher)
