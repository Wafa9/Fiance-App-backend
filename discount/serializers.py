from dataclasses import field
from rest_framework.serializers import ModelSerializer
from discount.models import Discount

class discountSerializer(ModelSerializer):
    class Meta:
        model=Discount
        fields=('key','website','code','icon','precent')