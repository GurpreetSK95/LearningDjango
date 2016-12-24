from django.conf.urls import url
from django.contrib import admin
from my_site.views import return_date, added_time, test_area
from books import views as views_books
from my_site import views as views_site


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^datetime/$', return_date),
    url(r'^datetime/plus/(\d{1,5})/$', added_time),  # value within () is offset
    # url(r'^$', hello)       # matches for root value
    url(r'^$', test_area),
    url(r'^search-form/$', views_books.search_form),
    url(r'^search/$', views_books.search),
    url(r'^contact/$', views_site.contact)
]
