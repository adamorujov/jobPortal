from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from jobportalapp.models import SiteSettings, PopularKeyword, Job, Contact, JobCategory, Company
from jobportalapp.api.serializers import (
    SiteSettingsSerializer, PopularKeywordSerializer, JobSerializer, 
    JobRetrieveSerializer, JobCreateSerializer, ContactSerializer, 
    UserCreateSerializer
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

class PopularKeywordListAPIView(ListAPIView):
    queryset = PopularKeyword.objects.all()
    serializer_class = PopularKeywordSerializer

class JobListAPIView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveAPIView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobRetrieveSerializer
    lookup_field = "id"

class JobCreateAPIView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer
    permission_classes = (IsAuthenticated,)

class RecentJobListAPIView(ListAPIView):
    queryset = Job.objects.all()[:10]
    serializer_class = JobSerializer

class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CategoryJobListAPIView(ListAPIView):
    def get_queryset(self):
        category_id = self.kwargs.get("id")
        category = JobCategory.objects.get(id=category_id)
        return Job.objects.filter(
            category = category
        )
    serializer_class = JobSerializer

class CompanyJobListAPIView(ListAPIView):
    def get_queryset(self):
        company_id = self.kwargs.get("id")
        company = Company.objects.get(id=company_id)
        return Job.objects.filter(
            company = company
        )
    serializer_class = JobSerializer