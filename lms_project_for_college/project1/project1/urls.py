from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('app1.urls')),
    path('lb1/',include('lb1.urls')),

]
