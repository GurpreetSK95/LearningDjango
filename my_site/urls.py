from django.conf.urls import url
from django.contrib import admin
from my_site.views import return_date, added_time

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^datetime/$', return_date),
    url(r'^datetime/plus/(\d{1,5})/$', added_time),  # value within () is offset
    # url(r'^$', hello)       # matches for root value
]
