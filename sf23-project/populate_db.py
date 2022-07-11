import pandas as pd
from expenseTracker.models import Expense


def loader():
    df = pd.read_csv("./expense_tracker.csv")
    for i in range(df.shape[0]):
        expenseModel = Expense()
        expenseModel.amount = df["Amount"][i]
        expenseModel.date = df["Date"][i]
        expenseModel.category = df["Category"][i]
        expenseModel.expense_type = df["Expense Type"][i]
        expenseModel.mode_of_payment = df["Mode of Payment"][i]
        expenseModel.save()


loader()
