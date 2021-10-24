from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.Todoview, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
