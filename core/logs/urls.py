from django.urls import path

from .views import files_status_view

urlpatterns = [
    path('my-files/', files_status_view, name='my-files'),
]
