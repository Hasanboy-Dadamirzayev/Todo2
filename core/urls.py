from django.contrib import admin
from main.views import *
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('task/<int:task_id>/confirm/', confirm_view, name='confirm'),
    path('task/<int:task_id>/delete/', delete_view, name='delete'),
    path('task/<int:task_id>/edit/', UpdateView.as_view(), name='edit'),
]

