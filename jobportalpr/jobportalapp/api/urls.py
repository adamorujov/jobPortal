from django.urls import path
from jobportalapp.api import views

urlpatterns = [
    path('settings/', views.SiteSettingsListAPIView.as_view()),
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('popular-keyword-list/', views.PopularKeywordListAPIView.as_view()),
    path('job-list/', views.JobListAPIView.as_view()),
    path('category-job-list/<int:id>/', views.CategoryJobListAPIView.as_view()),
    path('category-job-list/<int:category_id>/', views.CategoryJobListAPIView.as_view()),
    path('job-retrieve/<int:id>/', views.JobRetrieveAPIView.as_view()),
    path('job-create/', views.JobCreateAPIView.as_view()),
    path('recent-job-list/', views.RecentJobListAPIView.as_view()),
    path('contact-create/', views.ContactCreateAPIView.as_view()),
]

