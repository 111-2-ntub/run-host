from django.contrib import admin
from django.urls import path,include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('politician/',include("politician.urls")),
    path('user/',include("user.urls")),
    path('manage/',include("manager.urls")),
]
