from django.db import models
from HRmanagement.models import Employee

# Create your models here.


class InfoBase(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True


class Customer(InfoBase):  # 顾客信息表
    phone_number = models.IntegerField(verbose_name="联系电话")
    address = models.CharField(max_length=300, verbose_name="联系地址")
    account = models.CharField(db_index=True, max_length=50, verbose_name="账号名称")
    pwd = models.CharField(max_length=400, verbose_name="账户密码")
    gender = models.CharField(max_length=2, choices=(("1", "女"), ("2", "男"), ("3", "未设置")), default="3", verbose_name="性别")
    username = models.CharField(max_length=50, default=account, verbose_name="用户名称")
    customer_no = models.CharField(max_length=40, default=account, verbose_name="会员卡卡号")
    cust_score = models.IntegerField(verbose_name="消费积分")
    balance_of_const = models.IntegerField(verbose_name="消费余额")

    class Meta:
        verbose_name = "会员用户信息表"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

    def __str__(self):
        return self.username


class Production(InfoBase):  # 产品信息表
    prod_name = models.CharField(max_length=100, verbose_name="产品名称")
    prod_price = models.IntegerField(verbose_name="产品价格")
    prod_disc = models.IntegerField(verbose_name="产品折扣")

    class Meta:
        verbose_name = "产品信息表"
        verbose_name_plural = verbose_name
        ordering = ['-prod_name']

    def __str__(self):
        return self.prod_name


class LogofCons(models.Model):  # 消费信息表
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    operator = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True,to_field="employee_ID",
                                 verbose_name="操作员")
    order_list = models.CharField(max_length=800, verbose_name="消费信息")
    payment_method = models.CharField(max_length=200, choices=(("1", "现金"), ("2", "微信"), ("3", "支付宝"), ("4", "银联卡"),
                                                               ("5", "其他")), verbose_name="支付方式")

    class Meta:
        verbose_name = "消费信息表"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]
