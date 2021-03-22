"""prjdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prjdjango.views import greeting, goodbye, datetime, howOldAmI, sum, person, subjects
from orders.views import articles, search, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', articles),
    path('contact/', contact),
    path('greeting/', greeting),
    path('bye/', goodbye),
    path('datetime/', datetime),
    path('howOldAmI/<int:year>', howOldAmI),
    path('sum/<int:n1>/<int:n2>', sum),
    path('person/<name>/<lastname>', person),
    path('subjects/', subjects),
]
