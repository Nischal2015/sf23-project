from django import forms
from django.forms import ModelForm
from expenseTracker.models import Expense
from django.forms.widgets import DateInput, TextInput


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        # date = forms.DateField()
        fields = [
            "amount",
            "date",
            "category",
            "expense_type",
            "mode_of_payment",
            "remarks",
        ]
        widgets = {
            "date": DateInput(attrs={"type": "date"}),
            "remarks": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Name",
                }
            ),
        }
