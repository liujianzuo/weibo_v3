"""weibo URL Configuration

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

from web.home import account
from web.controller import controller as cont
from web.main import index as weibo_index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', account.login),
    url(r'^logout/', account.logout),
    url(r'^register/', account.register),
    url(r'^blog/', cont.blog),
    url(r'^pub/', cont.pub),
    url(r'^article/', cont.article),
<<<<<<< HEAD
# <<<<<<< HEAD
    url(r'^test/',account.test),
# =======
    url(r'^index/', weibo_index.index),
# <<<<<<< HEAD
    url(r'^lay_out/', weibo_index.lay_out),
    url(r'^test_lay_out/', weibo_index.test_lay_out),
# =======
# >>>>>>> f6efd67c2525c9ffc1c44b38a0dd4e541ab663f4
# >>>>>>> 7cb20227d6d21313dd1514355b23d570838579e7
=======

    url(r'^search/',account.search),

    url(r'^index/', weibo_index.index),
<<<<<<< HEAD

=======
<<<<<<< HEAD
    url(r'^lay_out/', weibo_index.lay_out),
    url(r'^test_lay_out/', weibo_index.test_lay_out),
=======
>>>>>>> f6efd67c2525c9ffc1c44b38a0dd4e541ab663f4
>>>>>>> 7cb20227d6d21313dd1514355b23d570838579e7
>>>>>>> 76a59e649662ce5dd89b25a195d6d5f82ee416c7
>>>>>>> 1813207509d9651a7f35420977702c978eab8d8e
]