from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authuser.urls')),
    path('', include('todo_app.urls')),
]
