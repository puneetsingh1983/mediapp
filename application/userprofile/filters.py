from django_filters import rest_framework as df_filters
from .models import DoctorProfile, HealthworkerProfile, PatientProfile


class DoctorFilter(df_filters.FilterSet):
    name = df_filters.CharFilter(lookup_expr='icontains')
    city = df_filters.CharFilter(field_name='address__city', lookup_expr='icontains')
    state = df_filters.CharFilter(field_name='address__state_id')
    country = df_filters.CharFilter(field_name='address__country_id')

    class Meta:
        model = DoctorProfile
        fields = ['name', 'years_of_experience', 'qualification', 'specialization', 'languages_can_speak',
                  'user__mobile', 'city', 'state']


class PatientFilter(df_filters.FilterSet):
    name = df_filters.CharFilter(lookup_expr='icontains')
    case_summary = df_filters.CharFilter(lookup_expr='icontains')
    city = df_filters.CharFilter(field_name='address__city', lookup_expr='icontains')
    state = df_filters.CharFilter(field_name='address__state_id')
    country = df_filters.CharFilter(field_name='address__country_id')

    class Meta:
        model = PatientProfile
        fields = ['case_summary', 'name', 'user__mobile', 'city', 'state', 'country']


class HealthworkerFilter(df_filters.FilterSet):
    name = df_filters.CharFilter(lookup_expr='icontains')
    city = df_filters.CharFilter(field_name='address__city', lookup_expr='icontains')
    state = df_filters.CharFilter(field_name='address__state_id')
    country = df_filters.CharFilter(field_name='address__country_id')

    class Meta:
        model = HealthworkerProfile
        fields = ['years_of_experience', 'qualification', 'languages_can_speak', 'user__mobile',
                  'city', 'state', 'country']