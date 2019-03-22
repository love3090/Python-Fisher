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
from SaleModule import views


app_name = "SaleModule"
urlpatterns = [
    # path(r'Sale/', include("SaleModule.urls")),
    re_path(r'dashboard/$', views.Dashboard.as_view(), name="Dashboard"),  # 主页面
    re_path('member_list/$', views.list_member, name="list_member"),  # 会员列表
    re_path('member_add/$', views.AddMember.as_view(), name="add_member"),  # 添加会员
    re_path('member_edit/<int:pk>/$', views.EditMember.as_view(), name="edit_member"),  # 会员信息编辑
    re_path('product_list/$', views.product_list, name="product_list"),  # 产品信息列表
    re_path('product_edit/<int:pk>/$', views.EditProduct.as_view(), name='edit_product'),
    re_path('product_add/$', views.AddProduct.as_view(), name='add_product'),
    # re_path(r'member_charge/(?(pk)\d+)', views.add_member, name="c_member"),  # 会员充值
]
# 下面语句可以使template的HTML文件找到static文件中的静态文件
urlpatterns += staticfiles_urlpatterns()
