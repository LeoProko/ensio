import django_filters
from crm.models import Order

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['item', 'status', 'phone_number']
