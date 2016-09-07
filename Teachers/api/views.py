#-*-coding:utf-8-*-

from rest_framework.generics import ListAPIView

from Teachers.models import Teacher

from .serializers import ListSerializer

class TeacherListAPIView(ListAPIView):
    queryset=Teacher.objects.all()
    serializer_class = ListSerializer

