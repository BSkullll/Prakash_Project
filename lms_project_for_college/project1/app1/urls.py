from django.urls import path
from . import views
urlpatterns = [


    path('home/',views.home,name="home"),
    path('e-lib/',views.e_lib,name="e-lib"),
    path('login/',views.login,name="login"),
    path('about/',views.about,name="about"),
    # path('signup/',views.signup),

]
