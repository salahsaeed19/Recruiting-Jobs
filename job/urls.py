from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('job/<int:pk>/', views.job_details, name="job_details"),
    path('home/<str:c>/', views.all_jobs, name="all_jobs"),
    path('offers/<int:id>', views.offers, name="offers"),
    path("signup/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("stttings/change_password/", auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html"), name="change_password"),
    path("stttings/change_password/done/", auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"),
    path("profile/", views.profile, name="profile"),
    path("profilee/", views.profilee, name="profilee"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
