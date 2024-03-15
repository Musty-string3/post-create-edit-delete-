from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('sample_app/', include('sample_app.urls')),
    path('admin/', admin.site.urls),
]
