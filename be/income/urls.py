from django.urls import path
from .views import IncomeListView, IncomeDetailView

urlpatterns = [
    path("", IncomeListView.as_view(), name="income-list"),
    path("<int:id>/", IncomeDetailView.as_view(), name="income-detail"),
]