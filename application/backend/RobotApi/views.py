#from mobility.robot_drive.robot_drive import RobotDrive
from django.http import HttpResponse
from rest_framework import generics

from . import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


def drive(request, code):
    print(request)
    print(code)
    return HttpResponse("Driving!")


def forward(request, speed):
    return HttpResponse("forward")


def backward(request, speed):
    return HttpResponse("backward")


def left(request, speed):
    return HttpResponse("left")


def right(request, speed):
    return HttpResponse("right")

