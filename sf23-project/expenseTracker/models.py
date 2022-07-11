from django.db import models

from django.db import models

# Create your models here.


CATEGORY_CHOICES = (
    ("Food", "Food"),
    ("Transportation", "Transportation"),
    ("Clothing", "Clothing"),
    ("Health", "Health"),
    ("Electronics", "Electronics"),
    ("Recreational", "Recreational"),
    ("Utility", "Utility"),
    ("Miscellaneous", "Miscellaneous"),
)
EXPENSE_TYPE_CHOICES = (
    ("Personal Use", "Personal Use"),
    ("Bill Sharing", "Bill Sharing"),
    ("Family Expense", "Family Expense"),
    ("Lend", "Lend"),
    ("Miscellaneous", "Miscellaneous"),
)

PAYMENT_CHOICES = (
    ("Cash", "Cash"),
    ("Credit Card", "Credit Card"),
    ("Online Payment", "Online Payment"),
)


class Expense(models.Model):
    """
    Expense model
    return: Expense object
    arguments:
    date: date of expense
    category: category of expense
    amount: amount of expense
    expense_type: type of expense
    payment_method: payment method of expense
    """

    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    expense_type = models.CharField(max_length=20, choices=EXPENSE_TYPE_CHOICES)
    mode_of_payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    remarks = models.CharField(null=True, blank=True, max_length=255)
