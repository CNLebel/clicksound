from django.shortcuts import render,redirect
from .froms import RegisterForm
from useradmin.models import *
# Create your views here.

# def login(request):
#     # all=UserInfo.objects.all()
#     pusername=request.POST.get('username')
#     # password=request.POST.get('password')
#     userk='tong981028@outlook.com'
#     passk='LItong1998'
#     # ba = UserInfo.objects.get('username')
#
#     if request.method == 'POST':
#         postData=request.POST
#         username=postData.get('username')
#         password=postData.get('password')
#
#
#         if username==userk and password==passk:
#
#             return redirect('/index')
#
#     # context={'username':username,'password':password,'all':all}
#     return render(request,'logins.html')


def register(request):

    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form=RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form=RegisterForm()


    return render(request, 'registration/register.html',context={'form': form, 'next': redirect_to})
