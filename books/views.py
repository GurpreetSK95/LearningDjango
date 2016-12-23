from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def search_form(request):
    return render(request, 'search_form.html')


'''
    In short:
    1. he HTML <form> defines a variable q. When it’s submitted, the value of q
        is sent via GET (method="get") to the URL /search/.
    2. The Django view that handles the URL /search/ (search()) has access to the q value in request.GET.
'''


def search(request):
    if 'query' in request.GET and request.GET['query']:
        q = request.GET['query']
        books = Book.objects.filter(title__icontains=q)  # find q in book titles, case insensitive
        return render(request, 'search_results.html', {'books': books, "query": q})
        # message = 'You searched for %r.' % request.GET['query']
    else:  # no if else will raise a KeyError
        message = 'Not found.'
    return HttpResponse(message)
