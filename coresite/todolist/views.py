
from .models import Todo
from django.shortcuts import render
from .serializer import TodoSerializer
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
import environ
# Create your views here.

env = environ.Env()
environ.Env.read_env()
test = env('TEST')
class TodoListAPIView(GenericAPIView, ListModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def get(self, request,*args, **kwargs):
        print(test)
        return self.list(request, *args, **kwargs)

def testview(request):
    return render(request, 'test.html')

# class CreateTodoAPIView(CreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

class CreateTodoAPIView(GenericAPIView, CreateModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RetrieveTodoAPIView(GenericAPIView, RetrieveModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer