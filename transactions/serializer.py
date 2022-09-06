from dataclasses import field
from rest_framework import serializers
from .models import Transaction, FinancialDeateails


class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class FinancialDeateailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialDeateails
        fields = '__all__'
