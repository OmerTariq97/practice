from .models import User, Comment
from userprofile.serializer import UserProfileSerializer
from rest_framework import serializers

class CreateUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True},
                        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']
        read_only_fields = ['user', 'created_at']