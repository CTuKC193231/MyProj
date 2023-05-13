from django.shortcuts import render, redirect
from myapp.models import Books, category, product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    new = Books()
    new.save()
    res = Books.objects.all()

    return render(request, 'index.html')



def reg(request):
    if request.method == "POST":
        data = request.POST
        new_user = User.objects.create_user(username=data["user"], password=data["password"])
        new_user.save()
    return render(request,"auth.html")

def auth(request):
    user = None
    if request.method == "POST":
        data = request.POST
        user = authenticate(username = data["user"],password = data["password"])
        if user is not None:
            request.session["is_auth"] = True
            print(user.get_username())
        else:
            return HttpResponse("Вы ошиблись ")

        
    return render(request,"auth.html",{"username":user})



def main(request):
    
    cat_list = category.objects.all()
    return render(request,'main.html',{"cat": cat_list,"req":request.session.get("is_auth", False)})


def cat_page(request,cat_name):
    catid = category.objects.filter(cat_name=cat_name)
    prod = product.objects.filter(cat_id = catid[0].id)
    return render(request, "cat_page.html", {"prod":prod})

def card_prod(request, urlp):
    if request.session.get("is_auth", False) == True:

        prod = product.objects.filter(id = urlp)
        return render(request,'prod_card.html',{"prod":prod,"req":request.session.get("is_auth", False)})
    else:
        return redirect("http://127.0.0.1:8000/auth/")  

    






