from rest_framework import serializers
from .models import TaskModel


class TaskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskModel
        fields = ('id', 'task_name', 'task_description', 'date_created', 'completed', 'images')
