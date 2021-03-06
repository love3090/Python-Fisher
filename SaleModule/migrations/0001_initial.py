# Generated by Django 2.1.2 on 2019-01-14 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HRmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('phone_number', models.IntegerField(verbose_name='联系电话')),
                ('address', models.CharField(max_length=300, verbose_name='联系地址')),
                ('account', models.CharField(db_index=True, max_length=50, verbose_name='账号名称')),
                ('pwd', models.CharField(max_length=400, verbose_name='账户密码')),
                ('gender', models.CharField(choices=[('1', '女'), ('2', '男'), ('3', '未设置')], default='3', max_length=2, verbose_name='性别')),
                ('username', models.CharField(default=models.CharField(db_index=True, max_length=50, verbose_name='账号名称'), max_length=50, verbose_name='用户名称')),
                ('customer_no', models.CharField(default=models.CharField(db_index=True, max_length=50, verbose_name='账号名称'), max_length=40, verbose_name='会员卡卡号')),
                ('cust_score', models.IntegerField(verbose_name='消费积分')),
                ('balance_of_const', models.IntegerField(verbose_name='消费余额')),
            ],
            options={
                'verbose_name': '会员用户信息表',
                'verbose_name_plural': '会员用户信息表',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='LogofCons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('order_list', models.CharField(max_length=800, verbose_name='消费信息')),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRmanagement.Employee', to_field='employee_ID', verbose_name='操作员')),
            ],
            options={
                'verbose_name': '消费信息表',
                'verbose_name_plural': '消费信息表',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('prod_name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('prod_price', models.IntegerField(verbose_name='产品价格')),
                ('prod_disc', models.IntegerField(verbose_name='产品折扣')),
            ],
            options={
                'verbose_name': '产品信息表',
                'verbose_name_plural': '产品信息表',
                'ordering': ['-prod_name'],
            },
        ),
    ]
