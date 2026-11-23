
from rest_framework import serializers

from subject.models import Course

class CourseSerializer(serializers.ModelSerializer):

    trainer = serializers.StringRelatedField()

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"]