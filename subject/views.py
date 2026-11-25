from django.shortcuts import render,get_object_or_404

from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from subject.models import Course
from subject.serializers import CourseSerializer
from subject.permissions import TrainerOnly

class CourseListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [TrainerOnly]

    serializer_class = CourseSerializer
    # queryset = Course.objects.all()

    def get_queryset(self):
        
        return Course.objects.filter(trainer=self.request.user)

class CourseCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = CourseSerializer

    def perform_create(self, serializer):

        serializer.save(trainer=self.request.user)

class CourseRetrieveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseUpdateDeleteView(UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [TrainerOnly]

    def put(self,request,pk=None):

        form_data = request.data

        instance = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = CourseSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message:deleted"})
    