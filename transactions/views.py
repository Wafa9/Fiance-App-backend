from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import TransactionsSerializer, FinancialDeateailsSerializer
from .models import Transaction, FinancialDeateails
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework import viewsets
import django_filters

# Create your views here.


class FinancialDeateailsFilterClass(django_filters.FilterSet):
    class Meta:
        model = FinancialDeateails
        fields = '__all__'


class TransactionViewset(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()
    permission_classes = [permissions.AllowAny, ]

    # def create(self, request, *args, **kwargs):
    #     print(request.POST)
    #     return super().create(request, *args, **kwargs)

    # def get_queryset(self):
    #     print(self.request.user)
    #     queryset = super().get_queryset().filter(owner=self.request.user)
    #     print(queryset)
    #     return queryset


# class TransactionDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = TransactionsSerializer
#     permission_classes = (permissions.AllowAny,)
#     queryset = Transaction.objects.all()
#     lookup_field = "id"

#     def get_queryset(self):
#         return self.queryset.filter(owner=self.request.user)


class FinancialDeateailsViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialDeateailsSerializer
    queryset = FinancialDeateails.objects.all()
    filter_class = FinancialDeateailsFilterClass
