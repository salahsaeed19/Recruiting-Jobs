from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import category as categorys
from .models import freelancer as freelancers
from .models import job as jobs
from .models import customer as user
from .models import apply 
from django.contrib.auth.models import User

def index(request):
    category = categorys.objects.all()
    job = jobs.objects.order_by('-id')[:5]
    freelancer = freelancers.objects.order_by('-id')[:10]
    context = {"category":category, "job": job, "freelancer": freelancer}

    return render(request, "pages/index.html", context)


def job_details(request, pk):
    
    if request.method =="POST":
        username = request.user # new column [know the owner of the offer]
        email = request.POST['email']
        link = request.POST['link']
        cv = request.POST['cv']
        coverletter = request.POST['coverletter']
        
        ap = apply.objects.create(
            username = username,
            email = email,
            link = link,
            cv = cv,
            coverletter = coverletter,
        )
        return redirect("index")
    job = jobs.objects.get(pk=pk)
    users = user.objects.get(pk=pk)
    context = {"job": job, "users": users}
    return render(request, "pages/job_details.html", context)


# def contact(request):
#     return render(request, "pages/contact.html")


# def signupcustomer(request):
#     form = SignUpCustomerForm()
#     if request.method == "POST":
#         form = SignUpCustomerForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect("index")
#     return render(request, "registration/signupcustomer.html", {"form": form})


def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    
    return render(request, "registration/profile.html")


def all_jobs(request,c):
    #free = freelancers.objects.all().filter(request.user.category)
    job = jobs.objects.order_by('-id')[:5]
    alljobs = jobs.objects.filter(
        category__name__contains=c)
    context = {
                "alljobs":alljobs,
                "job": job,
                #"free":free,
            }
    return render(request,"pages/a.html",context)


def offers(request,id):
    #x = request.GET['titl']
    #jobt=jobs.objects.filter(title=x)
    #offers = apply.objects.filter(job=jobt)
    #offers = apply.objects.all()
    jobb = jobs.objects.get(pk=id)
    free = apply.objects.filter(job=jobb)

    context = {
        "free":free
        
        }
    return render(request, "pages/offers.html", context)

def profilee(request):
    pass
#     free = apply.objects.filter(id=request.GET['id'])
#     return render(request, "registration/profilee.html",{"free":free})
