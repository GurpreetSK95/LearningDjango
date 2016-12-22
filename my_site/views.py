from django.http import HttpResponse, Http404
import datetime
from django import template
from django.template.loader import get_template


def hello(request):
    return HttpResponse("Hello World")


def return_date(request):
    # time = "The time is %s." % datetime.datetime.now()  # string formatting, datetime object converted to string by %s
    # templates should be stored in templates folder
    temp = get_template('return_date_template.html')
    context = template.Context({"time_now": datetime.datetime.now()})
    html = temp.render(context)
    return HttpResponse(html)


def added_time(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    future_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    statement = "The time in %s hour(s) will be %s" % (offset, future_time)
    return HttpResponse(statement)


def template_view(request):
    t = template.Template("My name is {{name}}.")
    context = template.Context({'name': "Gurpreet"})
    t.render(context)
