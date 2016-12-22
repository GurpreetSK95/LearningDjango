"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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
