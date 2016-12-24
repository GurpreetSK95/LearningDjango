from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
# from django import template
# from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from my_site.forms import ContactForm
from django.core.mail import send_mail


def return_date(request):
    # time = "The time is %s." % datetime.datetime.now()  # string formatting, datetime object converted to string by %s
    # templates should be stored in templates folder
    # temp = get_template('return_date_template.html')  # give absolute template path
    context = Context({"time_now": datetime.datetime.now(), "test": "test-test"})
    # html = temp.render(context)
    # return HttpResponse(html)

    # all the above code is replaced using render function
    return render(request, 'return_date_template.html', context)  # shortcut to return template


def added_time(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    future_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    context = Context({'n': offset, 'future_time': future_time})
    return render(request, 'added_time_template.html', context)


def test_area(request):  # META data test
    # NEVER TRUST BROWSER HEADER DATA - ALWAYS HANDLE EXCEPTIONS
    browser = request.META.get('HTTP_USER_AGENT', 'unknown browser')  # if an exception occurs, go with unknown
    referer = request.META.get('HTTP_REFERER', 'unknown referer')  # note spelling
    address = request.META.get('REMOTE_ADDR', 'unknown client IP address')

    # values = request.META.items() # get all meta items

    return HttpResponse(
        "Your browser is %s<br>Referrer is %s<br> Client IP is %s" % (browser, referer, address))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})    # initial value of form

    return render(request, 'contact_form.html', {'form': form})