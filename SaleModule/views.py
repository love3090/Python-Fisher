from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# Create your views here.


class Dashboard(View):
    def get(self, request):
        print("This is test syntax")
        # value = request.GET.
        return render(request, template_name="dashboard.html")

    def post(self, request):
        print("This is Post request!")
        return render(request, template_name="dashboard.html")


# def add_member(request):
#     print(request.method)
#     return render(request, template_name="member_add.html")

class AddMember(View):
    template_name = "member_add.html"

    def dispatch(self, request, *args, **kwargs):
        return super(AddMember, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return redirect("member_list")

    def get(self, request, *args, **kwargs):
        return render(request, "member_add.html")


def list_member(request):
    print(request.method)
    return render(request, template_name="member_list.html")

#
# def edit_member(request, pk):
#     obj = pk
#     print(request.method)
#     return render(request, template_name="member_edit.html")


class EditMember(View):
    """
    会员编辑功能，
    Method:Get方法获取编辑会员的页面，同时获取数据库中对应会员信息
    Method:Post方法用于提交编辑后的数据信息，并提交数据库中保存
    保存方法
    """
    template_name = "member_edit.html"

    def dispatch(self, request, *args, **kwargs):
        return super(EditMember, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass


def product_list(request):
    """
    产品或服务展示功能，
    Method:Get方法获取产品信息主要的页面，同时获取数据库中产品所有信息
    """
    print("这是产品列表")
    return render(request, template_name='product_list.html')


class EditProduct(View):
    """
    产品或服务编辑功能，
    Method:Get方法获取编辑产品的页面，同时获取数据库中对应产品信息
    Method:Post方法用于提交编辑后的数据信息，并提交数据库中保存
    保存方法为
    """
    def dispatch(self, request, *args, **kwargs):
        return super(EditProduct, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return render(request, template_name="product_list.html")

    def get(self, request, *args, **kwargs):
        return render(request, template_name='product_edit.html')


class AddProduct(View):
    def dispatch(self, request, *args, **kwargs):
        return super(AddProduct, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("这是产品内容新增表")
        return render(request, template_name='product_add.html')

    def post(self, request, *args, **kwargs):
        print("这是产品内容新增表后返回")
        return render(request,template_name="product_list.html")

