
from rest_framework import serializers

from accounts.models import User,TrainerProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

        read_only_fields = ["id","role"]

        
class TrainerProfileSerializer(serializers.ModelSerializer):

    trainer = serializers.StringRelatedField()

    class Meta:

        model = TrainerProfile

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"]        
        