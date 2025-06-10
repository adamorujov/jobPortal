from django.contrib import admin
from jobportalapp.models import PopularKeyword, JobCategory, Position, JobType, Tag, Company, Job, SiteSettings, Contact 

admin.site.register(PopularKeyword)
admin.site.register(JobCategory)
admin.site.register(Position)
admin.site.register(JobType)
admin.site.register(Tag)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(SiteSettings)
admin.site.register(Contact)

