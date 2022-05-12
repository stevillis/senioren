from django.urls import path

from .views.index_views import index

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
]
