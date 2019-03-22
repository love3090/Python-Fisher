from django.db import models

# Create your models here.


class InfoBase(models.Model):
    phone_number = models.IntegerField(verbose_name="联系电话")
    address = models.CharField(max_length=300, verbose_name="联系地址")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True


class StoreName(models.Model):
    store_name = models.CharField(max_length=20, verbose_name="店铺名称")
    department = models.CharField(max_length=50, unique=True, verbose_name="部门名称")

    class Meta:
        verbose_name = "门店信息表"


class Employee(InfoBase):  #职工信息表
    name = models.CharField(max_length=30, verbose_name="员工姓名")
    gender = models.CharField(max_length=2, choices=(("1", "女"), ("2", "男")), default="2", verbose_name="性别")
    employee_ID = models.CharField(max_length=20, unique=True, db_index=True, verbose_name="员工编号")
    department = models.ForeignKey(StoreName, to_field="department", on_delete=models.SET_NULL, null=True, max_length=20,
                                   verbose_name="所属店铺")
    postion = models.CharField(max_length=20, verbose_name="职位名称")

    class Meta:
        verbose_name = "职工信息表"


