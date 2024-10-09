from django.template.context_processors import request
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.status import HTTP_201_CREATED
from rest_framework.utils.representation import serializer_repr
from tutorial.quickstart.serializers import UserSerializer

from .models import User
from rest_framework.response import Response
from .serializer import CreateUserSerializer, ChangePasswordSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from userprofile.serializer import UserProfileSerializer


# Create your views here.

class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.validated_data.pop('profile', None)
        serializer.save()

        if profile:
            profile_serializer = UserProfileSerializer(data=profile)
            if profile_serializer.is_valid():
                profile_serializer.save(user=serializer.instance)

        return Response({
            "message": "User created successfully. Check your email for verification"
        }, status=HTTP_201_CREATED)

class ChangePasswordAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        self.object.set_password(serializer.data.get('new_password'))
        self.object.save()
        return Response('chaned')


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user to the currently authenticated user before saving the comment
        serializer.save(user=self.request.user)