#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from SaleModule import models


class CustomerForms(forms.Form):
    phone_number = forms.IntegerField(verbose_name="联系电话")
    account = forms.CharField(db_index=True, max_length=50, verbose_name="账号名称")
    pwd = forms.CharField(max_length=400, verbose_name="账户密码")
    username = forms.CharField(max_length=50, default=account, verbose_name="用户名称")
    balance_of_const = forms.IntegerField(verbose_name="消费余额")

    class Meta:
        model = models.Customer
