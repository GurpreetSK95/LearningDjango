from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello World!")


def return_date(request):
    time = "The time is %s." % datetime.datetime.now()  # string formatting, datetime object converted to string by %s
    return HttpResponse(time)


def added_time(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    future_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    statement = "The time in %s hour(s) will be %s" % (offset, future_time)
    return HttpResponse(statement)
