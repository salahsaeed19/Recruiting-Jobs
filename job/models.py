from django.db import models
from django.contrib.auth.models import User


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card = models.IntegerField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/customer/", null=True)
    # 1 customer many jobs --->  1 job 1 customer


    def __str__(self):
        return str(self.user.username)


class category(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name 


class freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card = models.IntegerField()
    name_job = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/freelancer/", null=True)
    category = models.ManyToManyField(category)


    def __str__(self):
        return str(self.user.username)


class job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=6000)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    salary = models.FloatField(blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(customer, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="img/post/", null=True)
    job_nature = models.CharField(max_length=30, null=True)
    # 1 customer many jobs --->  1 job 1 customer


    def __str__(self):
        return self.title

