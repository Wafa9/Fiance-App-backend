from django.shortcuts import render
from discount.models import Discount
from discount.serializers import discountSerializer
from rest_framework.generics import ListAPIView


class discountView(ListAPIView):
    serializer_class=discountSerializer
    queryset = Discount.objects.all()

    def get_queryset(self):
        return Discount.objects.all()

# Create your views here.
