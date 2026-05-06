from django.urls import path
from .views import transactions, delete_transaction

urlpatterns = [
    path('transactions/', transactions),
    path('transactions/<int:pk>/', delete_transaction),
]