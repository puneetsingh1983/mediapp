from django_filters import rest_framework as df_filters
from .models import Organization


class NumberInFilter(df_filters.BaseInFilter, df_filters.NumberFilter):
    pass


class OrganizationFilter(df_filters.FilterSet):
    org_type = df_filters.CharFilter(field_name='org_type__text', lookup_expr='iexact')
    name = df_filters.CharFilter(lookup_expr='icontains')
    specialization = NumberInFilter(field_name='specialization', lookup_expr='in')
    specialization_text = df_filters.CharFilter(field_name='specialization__text', lookup_expr='icontains')

    class Meta:
        model = Organization
        fields = ['org_type', 'name', 'specialization_text', 'specialization']


