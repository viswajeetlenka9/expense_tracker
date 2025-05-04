from django.urls import path
from .views import ExpenseListView, ExpenseDetailView

urlpatterns = [
    path("", ExpenseListView.as_view(), name="expense-list"),
    path("<int:id>/", ExpenseDetailView.as_view(), name="expense-detail"),
]