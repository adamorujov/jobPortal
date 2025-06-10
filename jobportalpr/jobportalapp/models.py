from django.db import models
from tinymce.models import HTMLField

class PopularKeyword(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class JobCategory(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=30)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class Position(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class JobType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="company_imgs/")
    about = HTMLField(blank=True, null=True)
    website = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)

    class Meta:
        verbose_name_plural = "Companies"


    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    location = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=20)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, related_name="position_jobs", blank=True, null=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, related_name="type_jobs", blank=True, null=True)
    description = HTMLField()
    tags = models.ManyToManyField(Tag, related_name="jobs")
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, related_name="jobs", blank=True, null=True)

    def __str__(self):
        return self.title
    
class SiteSettings(models.Model):
    favicon = models.ImageField(upload_to="site_imgs/", blank=True, null=True)
    logo = models.ImageField(upload_to="site_imgs/", blank=True, null=True)
    banner_title = models.TextField(blank=True, null=True)
    banner_content = models.TextField(blank=True, null=True)

    middle_title = models.TextField(blank=True, null=True)
    middle_content = models.TextField(blank=True, null=True)
    middle_image_1 = models.ImageField(upload_to="site_imgs/", blank=True, null=True)
    middle_image_2 = models.ImageField(upload_to="site_imgs/", blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    middle_position = models.CharField(max_length=50, blank=True, null=True)

    featured_jobs_content = models.TextField(blank=True, null=True)

    bottom_title = models.TextField(blank=True, null=True)
    bottom_content = models.TextField(blank=True, null=True)
    daily_active_users = models.FloatField(blank=True, null=True)
    opening_jobs = models.FloatField(blank=True, null=True)
    bottom_image = models.ImageField(upload_to="site_imgs/", blank=True, null=True)
    bottom_video_link = models.TextField(blank=True, null=True)

    recent_jobs_content = models.TextField(blank=True, null=True)

    ebottom_title = models.TextField(blank=True, null=True)
    ebottom_content = models.TextField(blank=True, null=True)
    ebottom_image = models.ImageField(upload_to="site_imgs/", blank=True, null=True)

    website = models.TextField(blank=True, null=True)
    contact_number = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    office_location = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    def __str__(self):
        return "Settings"
    
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings, self).save(*args, **kwargs)
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
        
"""
Job - many    -----       Position - one
Job - many  --------      Job Type  - one
Job - many    ---------   Tag - many
Job - many  --------      Company - one


Job - many     ---------   Category  - one


"""