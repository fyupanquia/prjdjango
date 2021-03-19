from django.http import HttpResponse
from datetime import date
from datetime import datetime as dt
from django.template import Template, Context, loader
from django.shortcuts import render

template = open('G:/prjs/python/prjdjango/prjdjango/templates/main.html')
plt = Template(template.read())
template.close()


class Person(object):
    def __init__(self, name, lastname):
        self.name=name
        self.lastname = lastname
    
    def sayHello(self):
        return f"Hello! my name is {self.name} {self.lastname}"

def greeting(request):
    args = {"message": "Hi universe!"}
    #ctx=Context(args)
    #doc=plt.render(ctx)
    #return HttpResponse(doc)

    #template=loader.get_template('main.html')
    #doc = template.render(args)
    #return HttpResponse(doc)

    return render(request, "main.html", args)


def goodbye(request):

    return render(request, "goodbye/index.html", {"message":"Good bye sir!"})


def person(request, name, lastname):
    p = Person(name, lastname)
    ctx = Context({"message": p.sayHello()})
    doc = plt.render(ctx)
    return HttpResponse(doc)

def datetime(request):
    today = date.today().strftime("%d/%m/%Y")
    now = dt.now()
    print("today =", today)
    ctx = Context({"message": now})
    doc=plt.render(ctx)
    return HttpResponse(doc)

def howOldAmI(request, year):
    current_year = int(date.today().strftime("%Y"))
    diff = current_year - year
    message = "You're %s years old" % diff
    ctx = Context({"message": message})
    doc=plt.render(ctx)
    return HttpResponse(doc)


def sum(request, n1,n2):
    ctx = Context({"message": (n1+n2)})
    doc = plt.render(ctx)
    return HttpResponse(doc)


def subjects(request):
    languages = ['php','javascript','python','java'] 
    ctx = Context({"list": languages,"message":"subjects!"})
    doc = plt.render(ctx)
    return HttpResponse(doc)
