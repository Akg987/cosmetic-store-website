from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from . import forms
from homepage.models import cosmetics
from .UserAuth import UserAuth
from .models import ask
from .forms import asked,cosmeticForm
from django.core import serializers
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Cosmetics = cosmetics.objects.all()
        return render(request=request, template_name='home.html', context={"user_st":user_st,"cosmetics":Cosmetics})
    else:
        Cosmetics = cosmetics.objects.all()
        return render(request=request, template_name='home.html', context={"user_st":user_st,"cosmetics":Cosmetics})


def createcosmetic(request):
    if request.method == 'POST':
        forms = cosmeticForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
        else:
            forms = cosmeticForm()
            return render(request, template_name='createcosmetics.html', context={'forms': forms})
    forms = cosmeticForm()
    return render(request,template_name='createcosmetics.html',context={'forms':forms})


def readallcosmetics(request):
    if request.method == "POST":
        if str(request.POST.get("tokens")) == "aref21312kodp&(3423&":
            user_st = UserAuth().StateLogin(request)
            if user_st["State"]:
                search = request.POST.get("search", "")

                if search:
                    listData = cosmetics.objects.filter(title__icontains=search)
                else:
                    listData = cosmetics.objects.all()

                myserData = serializers.serialize("json", listData)
                return HttpResponse(myserData, content_type="application/json")
    return HttpResponse("403", status=403)

def productdetails(request, id):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        product = cosmetics.objects.get(id=id)
        reviews = ask.objects.filter(product_id=id)
        form_reviews = asked(initial={'product_id': id})
        return render(request, template_name='productdetails.html', context={
            "user_st": user_st,
            "forms": product,
            "reviews": reviews,
            "formReviews": form_reviews,
            'product_id': id
        })


def saveAsk(request, id):
    if request.method == "POST":
        print("POST request received")
        form = asked(request.POST)
        if form.is_valid():
            print("Form is valid")
            user_st = UserAuth().StateLogin(request)
            product = cosmetics.objects.get(id=id)
            if product:
                id_field = form.cleaned_data["id"]
                if id_field == 0:
                    datast = ask.objects.filter(title=form.cleaned_data["title"]).exists()
                    if datast:
                        print("Review with this title already exists")
                        return HttpResponse("exists")
                    x = datetime.datetime.now()
                    asknew = ask(
                        title=form.cleaned_data["title"],
                        caption=form.cleaned_data["caption"],
                        user=user_st["User"],
                        Created=x,
                        product=product
                    )
                    asknew.save()
                    print("Review saved successfully")
                    return HttpResponse("True")
                else:
                    askedit = ask.objects.filter(id=id_field).first()
                    if askedit:
                        askedit.title = form.cleaned_data["title"]
                        askedit.caption = form.cleaned_data["caption"]
                        askedit.save()
                        print("Review updated successfully")
                        return HttpResponse("True")
            else:
                print("Product not found")
                return HttpResponse("false")
        else:
            print(form.errors)
            return HttpResponse("valid")
    else:
        print("Not a POST request")
        return HttpResponse("false")




def readallAsk(request, id):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            listData = ask.objects.filter(product_id=id).values('title', 'caption', 'Created').all()
            print(listData)
            return JsonResponse(list(listData), safe=False)
    return JsonResponse({"error": "Forbidden"}, status=403)

def profile(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        return render(request=request, template_name='profile.html')
    else:
        return HttpResponse("403")

