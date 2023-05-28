from django.contrib import admin
from django.urls import include, path
from post.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('', home, name='home'),
]
