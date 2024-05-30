from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('tickets/', include('tickets.urls')),
    path('chat/', include('chat.urls')),

]
