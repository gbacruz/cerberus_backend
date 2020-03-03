
'''
THE VIEWS
'''
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import  JsonResponse

from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.settings import api_settings

from webapp.serializers import UserSzer
from webapp.serializers import IsintomSzer, ImeasureSzer 
from inteligence.models import Isintom, Imeasure
'''


'''

class IsintomV(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Isintom.objects.all()
    serializer_class = IsintomSzer

    def get(self, request,pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class MeasureV(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Imeasure.objects.all()
    serializer_class = ImeasureSzer

    def get(self, request,pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
