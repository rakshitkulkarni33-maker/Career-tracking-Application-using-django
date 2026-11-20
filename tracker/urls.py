from django.urls import path
from . import views
urlpatterns=[
 path("",views.home,name="home"),path("signup/",views.signup,name="signup"),
 path("login/",views.login_view,name="login"),path("logout/",views.logout_view,name="logout"),
 path("dashboard/",views.dashboard,name="dashboard"),path("applications/",views.application_list,name="applications"),
 path("applications/add/",views.application_create,name="application_add"),
 path("applications/<int:pk>/edit/",views.application_edit,name="application_edit"),
 path("applications/<int:pk>/delete/",views.application_delete,name="application_delete"),
]
