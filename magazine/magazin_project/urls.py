from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('magazine_app.urls')),  # Inclui as URLs do aplicativo magazine_app
]

