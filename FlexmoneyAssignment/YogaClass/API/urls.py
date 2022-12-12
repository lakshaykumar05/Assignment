from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', views.ValidateAndSaveData),
    # path('pay/',views.CompletePayment)
]
