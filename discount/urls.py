from django.urls import path
from .views import discountView

urlpatterns = [
    path('codes/', discountView.as_view(), name="codes")
]