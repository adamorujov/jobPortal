from rest_framework import serializers
from jobportalapp.models import SiteSettings, PopularKeyword, Job, Position, Tag, Contact, JobCategory
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("username", "email", "password")

    """
    data = {
        "username": "user1",
        "email": "user1@gmail.com",
        "password": ""
    }
    
    """

    def validate(self, data):
        validate_password(data["password"])
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        return user



class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"

class PopularKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularKeyword
        fields = "__all__"

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    category = JobCategorySerializer()

    class Meta:
        model = Job
        fields = ('title', 'location', 'created_at', 'salary', 'position', 'job_type', 'company', 'category')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class JobRetrieveSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    tags = TagSerializer(many=True)
    similar_jobs = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"

    def get_similar_jobs(self, obj):
        similar_jobs = Job.objects.filter(
            tags__in = obj.tags.all()
        )
        return JobSerializer(similar_jobs, many=True).data
    
class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
