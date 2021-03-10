from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ("user",)

    def create(self, validated_data):
        request = self.context["request"]
        validated_data['user'] = request.user

        return super(TaskSerializer, self).create(validated_data)
