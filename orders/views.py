from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Article
from django.core.mail import send_mail
from django.conf import settings
from orders.forms import ContactForm
# Create your views here.


def articles(request):
    error_message = ""
    name = request.GET.get("name", "")

    if len(name) >20:
        error_message = "too long search text"
        name=""
    
    if len(name) > 0 and len(name) < 20:
        # if name:
        articles = Article.objects.filter(name__icontains=name)
    else:
        articles = Article.objects.all()

    return render(request, "product.list.html",
                  {"articles": articles,
                   "name": name,
                   "error_message": error_message
                   })


def search(request):
    name = request.GET["name"]
    article = Article.objects.filter(name__icontrains=article)
    return render(request, "product.list.html", {"article": article, "name": name})


def contact(request):
    if(request.method=="POST"):
        
        #subject=request.POST["subject"]
        #message=request.POST["message"] + "\n" + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list = [""]
        #send_mail(subject, message, email_from, recipient_list)
        
        form=ContactForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data

            send_mail(data["subject"], data["message"], email_from, recipient_list)
            return render(request, "thankyou.html")

    #return  render(request, "contact.html")
    html=ContactForm()
    return render(request, "contact.html", {"form":html})

