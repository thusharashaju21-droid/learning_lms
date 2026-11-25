from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from units.models import Modules
from units.serializers import ModuleSerializer
from units.permissions import ModuleTrainerOnly

from subject.permissions import TrainerOnly

from subject.models import Course

class ModuleCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [TrainerOnly]

    def post(self,request,pk=None):

        course_id = pk
        course_object = Course.objects.filter(id=course_id).first()

        form_data = request.data

        # validation start

        if course_object is None:

            raise serializers.ValidationError("Invalid course, course does not exist")

        # validation end

        self.check_object_permissions(request,course_object)

        serializer_instance = ModuleSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(course=course_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class ModuleRetreiveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [ModuleTrainerOnly]

    serializer_class = ModuleSerializer
    queryset = Modules.objects.all()
    