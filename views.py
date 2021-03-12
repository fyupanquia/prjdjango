from django.http import HttpResponse
from datetime import date
from datetime import datetime as dt

doc = """
        <html>
            <body>
            <b>%s</b>
            </body>
        </html>
    """


def greeting(request):
    return HttpResponse(doc % 'Hi everyone!')


def goodbye(request):
    return HttpResponse('Good Bye!')


def datetime(request):
    today = date.today().strftime("%d/%m/%Y")
    now = dt.now()
    print("today =", today)
    return HttpResponse(doc % now)

def howOldAmI(request, year):
    current_year = int(date.today().strftime("%Y"))
    diff = current_year - year
    message = "You're %s years old" % diff
    return HttpResponse(doc % message)


def sum(request, n1,n2):
    return HttpResponse(doc % (n1+n2))
