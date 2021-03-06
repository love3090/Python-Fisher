"""MemberShipSystem URL Configuration

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

from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from basecontent.views import LoginOperat


app_name = "SaleModule"
urlpatterns = [
    # path(r'Sale/', include("SaleModule.urls")),
    path('Login/', LoginOperat.as_view(), name="Login"),
]
# 下面语句可以使template的HTML文件找到static文件中的静态文件
urlpatterns += staticfiles_urlpatterns()