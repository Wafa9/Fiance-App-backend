from datetime import date
from tkinter import CASCADE
from django.db import models
from authentication.models import User


# Create your models here.
# Create your models here.

class Transaction(models.Model):

    TYPE_OPTIONS = [
        ('BALANCE', 'BALANCE'),
        ('SAVING', 'SAVING'),
        ('LOANS', 'LOANS'),
        ('INCOME', 'INCOME'),
        ('EXPENSES', 'EXPENSES')
    ]

    type = models.CharField(choices=TYPE_OPTIONS, max_length=255)
    amount = models.IntegerField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    date = models.CharField(max_length=255)


class FinancialDeateails(models.Model):
    balance = models.IntegerField(max_length=255)
    savaing = models.IntegerField(max_length=255)
    income = models.IntegerField(max_length=255)
    loans = models.IntegerField(max_length=255)
    expenses = models.IntegerField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
