"""family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from familydata.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', home, name='home'),
    url('^family_list/$', family_list, name='list'),
    url('^news/$', news, name='news'),
    url('^family_list/id=(\d+)/$', detail, name='detail'),
    url('^quadric/results/', quadric, name='quadro'),
    url('^forms$', get_forms, name='forms'),
]
