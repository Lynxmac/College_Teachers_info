#-*-coding:utf-8-*-

from rest_framework.serializers import ModelSerializer

from Teachers.models import Teacher


class ListSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "name",
            "slug",
            "image",
        ]

