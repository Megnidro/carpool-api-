import django_filters
from .models import Trip


class TripFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter(field_name='start_time', lookup_expr='exact')
    start_time__gte = django_filters.DateTimeFilter(field_name='start_time', lookup_expr='gte')
    start_time__lte = django_filters.DateTimeFilter(field_name='start_time', lookup_expr='lte')
    end_time = django_filters.DateTimeFilter(field_name='end_time', lookup_expr='exact')
    end_time__gte = django_filters.DateTimeFilter(field_name='end_time', lookup_expr='gte')
    end_time__lte = django_filters.DateTimeFilter(field_name='end_time', lookup_expr='lte')

    class Meta:
        model = Trip
        fields = {
            'status': ['exact'],
            'start_location': ['icontains'],
            'end_location': ['icontains'],
            'seats': ['exact', 'gte', 'lte'],
            'driver': ['exact'],
            'car': ['exact'],
        }
