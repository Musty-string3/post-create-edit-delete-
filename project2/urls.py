from django.contrib import admin
from django.urls import path, include
from project2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_app/', include('sample_app.urls')),
    path('admin/', admin.site.urls),
]
