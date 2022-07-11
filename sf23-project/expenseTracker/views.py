from django.shortcuts import render, redirect
import json
from expenseTracker.forms import ExpenseForm
from expenseTracker.models import Expense
from django.db.models import Count, Sum


# bar chart
def mode_of_payment():
    # expense = Expense.objects.all()
    qs = Expense.objects.all().values("mode_of_payment").annotate(total=Sum("amount"))
    result_x = []
    result_y = []
    for item in qs:
        result_x.append(item["mode_of_payment"])
        result_y.append(item["total"])
    return {"x_values": result_x, "y_values": result_y}


def expense_category():
    qs = Expense.objects.all().values("category").annotate(total=Sum("amount"))
    result_x = []
    result_y = []
    for item in qs:
        result_x.append(item["category"])
        result_y.append(item["total"])
    return {"x_values": result_x, "y_values": result_y}

# pie chart 
def expense_type():
    qs = Expense.objects.all().values("expense_type").annotate(total=Sum("amount"))
    result_x = []
    result_y = []
    for item in qs:
        result_x.append(item["expense_type"])
        result_y.append(item["total"])
    return {"x_values": result_x, "y_values": result_y}


def expense_date():
    qs = Expense.objects.all().values("date").annotate(total=Sum("amount"))
    result_x = []
    result_y = []
    for item in qs:
        result_x.append(item["date"].strftime("%m/%d/%Y"))
        result_y.append(item["total"])
    return {"x_values": result_x, "y_values": result_y}


# Create your views here.
def dashboard(request):
    context = {}
    context["graph1"] = mode_of_payment()
    context["graph2"] = expense_type()
    context["graph3"] = expense_category()
    context["graph4"] = expense_date()
    return render(
        request,
        "expenseTracker/dashboard.html",
        context={"context": json.dumps(context)},
    )


def add_expense(request):
    form = ExpenseForm()

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dashboard)
    else:
        context = {"form": form}
        return render(request, "expenseTracker/add_expense.html", context)