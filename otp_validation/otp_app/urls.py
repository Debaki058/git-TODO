from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.signup, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("login", views.signin, name="signin"),
    path("std/home/",views.home),
    path("std/add_std/",views.std_add),
    path("std/delete-std/<int:roll>",views.delete_std),
    path("std/update-std/<int:roll>",views.update_std),
    path("std/do-update-std/<int:roll>",views.do_update_std),
]