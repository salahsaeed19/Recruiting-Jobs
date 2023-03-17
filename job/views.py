from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, CustomerForm, FreelancerForm, JobForm
from .models import customer, apply, job as jobs, freelancer as freelancers, category as categorys
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def index(request):
    category = categorys.objects.all()
    job = jobs.objects.order_by('id')[:6]
    freelancer = freelancers.objects.order_by('-id')[:10]
    context = {"category":category, "job": job, "freelancer": freelancer}
    return render(request, "pages/index.html", context)


@login_required
def job_details(request, pk):
    if request.method =="POST":
        test = freelancers.objects.filter(user = request.user).count()
        if test :
            username = request.user # new column [know the owner of the offer]
            email = request.POST['email']
            link = request.POST['link']
            cv = request.FILES['cv']
            coverletter = request.POST['coverletter']
            job = jobs.objects.get(pk=pk)
            ap = apply.objects.create(
                username = username,
                email = email,
                link = link,
                cv = cv,
                coverletter = coverletter,
                job=job,
            )
            return redirect("index")
        else:
            return redirect("add_freelancer")
    job = jobs.objects.get(pk=pk)
    users = customer.objects.get(pk=pk)
    context = {"job": job, "users": users}
    return render(request, "pages/job_details.html", context)


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
def all_jobs(request,c):
    alljobs=categorys.objects.all()
    job = jobs.objects.order_by('-id')[:5]
    alljobs = jobs.objects.filter(
        category__name__contains=c)
    context = {
                "alljobs":alljobs,
                "job": job,
            }
    return render(request,"pages/a.html",context)


@login_required
def offers(request,id):
    jobb = jobs.objects.get(pk=id)
    free = apply.objects.filter(job=jobb)
    count = len(free)
    context = {
        "free":free,
        "count": count
        }
    return render(request, "pages/offers.html", context)


@login_required
def profile(request, name):
    users = User.objects.get(username=name)
    context = {"users": users}
    if users == request.user:
        f = freelancers.objects.filter(user = users)
        return render(request, "registration/profile.html", {"users": users,"f": f})
    return render(request, "registration/profile.html", context)


@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('index')
    else:
        form = CustomerForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/add_customer.html', context)


@login_required
def add_freelancer(request):
    if request.method == 'POST':
        form = FreelancerForm(request.POST, request.FILES)
        if form.is_valid():
            freelancer = form.save(commit=False)
            freelancer.user = request.user
            freelancer.save()
            return redirect('index')
    else:
        form = FreelancerForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/add_freelancer.html', context)


@login_required
def createjob(request):
    test = customer.objects.filter(user = request.user).count()
    if request.method =="POST":
        if test:
            form = JobForm(request.POST,request.FILES)
            if form.is_valid():
                job = form.save(commit=False)
                job.created_by = request.user.customer
                job.save()
                return redirect('index')
        else:
            return redirect('add_customer')
    else:
        form =JobForm()
    context = {
        'form': form,
        }
    return render(request, 'pages/create_job.html', context)   


def browse_more_job(request):
    job = jobs.objects.order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(job, 6)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)
    return render(request,'pages/browse_more_job.html',{'job':job, 'topics':topics})
