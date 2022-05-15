from django.urls import path

from .views.medicine_views import (MedicineListView, create_medicine,
                                   deactivate_medicine, list_medicines,
                                   medicine_detail, update_medicine)

app_name = 'medicine'

urlpatterns = [
    path('medicine/list/', list_medicines, name='list'),
    path('medicine/detail/<int:pk>/', medicine_detail, name='detail'),
    path('medicine/create/', create_medicine, name='create'),
    path('medicine/update/<int:pk>/', update_medicine, name='update'),
    path('medicine/deactivate/<int:pk>/', deactivate_medicine, name='deactivate'),
    path('medicine/data/', MedicineListView.as_view(), name='data'),
]
