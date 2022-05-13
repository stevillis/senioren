from django.urls import path

from .views.medicine_views import (create_medicine, deactivate_medicine,
                                   list_medicines, medicine_detail,
                                   update_medicine)

app_name = 'medicine'

urlpatterns = [
    path('list/', list_medicines, name='list'),
    path('detail/<int:pk>/', medicine_detail, name='detail'),
    path('create/', create_medicine, name='create'),
    path('update/<int:pk>/', update_medicine, name='update'),
    path('deactivate/<int:pk>/', deactivate_medicine, name='deactivate'),
]
