from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Register
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from homepage.views import homepage
# Create your views here.
def logins(request):
    forms=Login()
    return render(request=request,template_name="login.html",context={"forms":forms})

def register(request):
    forms=Register()
    return render(request=request,template_name="register.html",context={"forms":forms})



def checklogin(request):
    forms=Login(request.POST)
    if forms.is_valid():
        username = forms.cleaned_data["UserName"]
        password = forms.cleaned_data["Password"]
        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/homepage")
        else:
            return HttpResponse("حسابی با این مشحصات یافت نشد")
    else:
        return HttpResponse("مشکلی پیش امده است")

def LogOut(request):
    logout(request)
    return HttpResponseRedirect("/auth/")

def registerAction(request):
    if request.method=="POST":
        forms = Register(request.POST)
        if forms.is_valid():
            users=User.objects.filter(username=forms.data["UserName"]).all()
            if len(users)>0:
                return HttpResponse("این کاربر در سیستم وجود دارد")
            else:

                us=User.objects.create_user(forms.data["UserName"],forms.data["Email"],forms.data["Password"])
                us.username=forms.data["UserName"]
                us.Password=forms.data["Password"]
                us.save()
                return HttpResponse("کاربر ساخته شد")
        else:
            return HttpResponse("فرم نا معتبر است")
def CheckAuth(request):
    if request.user.is_authenticated:
       return HttpResponse("وارد شده است")
    else:
       return HttpResponse("وارد نشده است")

def getCookies(request):
    return HttpResponse(request.COOKIES["UserName"])

def checkloginAjaxs(request, UserName, Password):

    username = UserName
    password = Password

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse("خوش امدید اطلاعات معتبر است ")
    else:
        return HttpResponse("حسابی با این مشحصات یافت نشد")