from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('finance', views.FinancialDeateailsViewSet, 'finance')
router.register('', views.TransactionViewset, 'transactions')


urlpatterns = [
    path('', include(router.urls)),
    # path('list/', views.TransactionList.as_view(), name="transactions"),
    # path('<int:id>', views.TransactionDetailAPIView.as_view(), name="transaction"),
]
