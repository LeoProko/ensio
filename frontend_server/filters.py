import django_filters
from .models import Order, Item

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date_created', lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created']

class ItemFilter(django_filters.FilterSet):
    min_stock = django_filters.NumberFilter(field_name='stock_balance', lookup_expr='gte')
    max_stock = django_filters.NumberFilter(field_name='stock_balance', lookup_expr='lte')
    class Meta:
        model = Item
        fields = ['name', 'price', 'tags', 'stock_balance']
        exclude = ['stock_balance']
