from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import category as categorys
from .models import freelancer as freelancers
from .models import job as jobs
from .models import customer as user


def index(request):
    category = categorys.objects.all()
    job = jobs.objects.order_by('-id')[:5]
    freelancer = freelancers.objects.order_by('-id')[:10]
    context = {"category":category, "job": job, "freelancer": freelancer}

    return render(request, "pages/index.html", context)


def job_details(request, pk):
    job = jobs.objects.get(pk=pk)
    users = user.objects.get(pk=pk)
    context = {"job": job, "users": users}
    return render(request, "pages/job_details.html", context)


# def contact(request):
#     return render(request, "pages/contact.html")


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

