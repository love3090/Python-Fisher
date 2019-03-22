from django.shortcuts import render, redirect
from django.views import View


# Create your views here.


class LoginOperat(View):

    def get(self, request):
        """
        Manager input the username and password when he login the Login.html
        :param request: get the request's url
        :return: Login.html
        """

        return render(request, template_name="Login.html")

    def post(self, request):
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        return redirect(request, "dashboar.html")