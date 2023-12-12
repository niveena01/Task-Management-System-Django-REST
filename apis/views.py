from rest_framework import viewsets
from .models import TaskModel
from .serializers import TaskSerializers


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = TaskModel.objects.all()

    # specify serializer to be used
    serializer_class = TaskSerializers

