
from rest_framework import serializers

from subject.models import Course
from units.models import Modules
from units.serializers import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):

    trainer = serializers.StringRelatedField(read_only=True)
    modules = serializers.SerializerMethodField(read_only=True)
    module_count = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"]

    def get_modules(self,obj):

        module_object = Modules.objects.filter(course=obj)

        serializer_instance = ModuleSerializer(module_object,many=True)

        return serializer_instance.data

    def get_module_count(self,obj):

        return Modules.objects.filter(course=obj).count()
    