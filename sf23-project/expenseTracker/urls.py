from django.urls import path
from expenseTracker import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add_expense", views.add_expense, name="add_expense"),
]
