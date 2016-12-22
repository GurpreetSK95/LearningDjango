from django.conf.urls import url
from django.contrib import admin
from my_site.views import hello, return_date, added_time, template_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),  # /hello/ should be the exact value, as in www. google.com/hello
    url(r'^datetime/$', return_date),
    url(r'^datetime/plus/(\d{1,5})/$', added_time),  # value within () is offset
    url(r'^template/$', template_view)
    # url(r'^$', hello)       # matches for root value
]
