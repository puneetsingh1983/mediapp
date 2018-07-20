from django_filters import rest_framework as df_filters
from .models import DoctorProfile, HealthworkerProfile, PatientProfile


class DoctorFilter(df_filters.FilterSet):
    name = df_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DoctorProfile
        fields = ['name', 'years_of_experience', 'qualification', 'specialization', 'languages_can_speak',
                  'user__mobile']


class PatientFilter(df_filters.FilterSet):
    name = df_filters.CharFilter(lookup_expr='icontains')
    case_summary = df_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PatientProfile
        fields = ['case_summary', 'name', 'user__mobile']


class HealthworkerFilter(df_filters.FilterSet):
    name = df_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = HealthworkerProfile
        fields = ['years_of_experience', 'qualification', 'languages_can_speak', 'user__mobile']