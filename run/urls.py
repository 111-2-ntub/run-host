from django.contrib import admin
from django.urls import path,include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p/',include("politician.urls")),
    path('u/',include("user.urls")),
]
