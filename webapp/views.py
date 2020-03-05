from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import status

from django.http import  JsonResponse

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

import simplejson
from webapp.models import (Consulta, Sintom, Patient, Medic, Attend)

from webapp.serializers import (UserSzer, ConsultaSzer, PatientSzer,
                                SintomSzer, MedicSzer, AttendSzer,
                                setConsultaSzer, SingleConsultaSzer)


'''
    HERE, you could add elements of a navigation structure, divides into:
    MAINSECTION (as usual, not navegable mode)
    COLUMNS, a division on to menu area
    section, the navegable page

'''

class getMyPatients(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSzer

    def get(self, request, pk=None, *args, **kwargs):
        self.queryset = Patient.objects.filter(userpk_id=pk)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class getPatients(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSzer

    def get(self, request, pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Medicinfo(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Medic.objects.all()
    serializer_class = MedicSzer

    def get(self, request, pk=0, *args, **kwargs):
        if pk > 0: 
            self.queryset = Medic.objects.filter(userpk_id=pk)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class getConsulta(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Consulta.objects.filter(date_end__isnull=True)
    serializer_class = ConsultaSzer

    def get(self, request, pk=None, *args, **kwargs):
        upk = request.GET.get('upk', None)
        if upk: 
            self.queryset = Consulta.objects.all().exclude(consulta_atendida__attended_id=upk)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class addSintom(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Sintom.objects.all()
    serializer_class = SintomSzer

    def get(self, request, pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, pk=None, *args, **kwargs):
        event = self.get_object()
        event.delete()
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class getUser(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSzer

    def post(self, request,pk=None, *args, **kwargs):
        user = request.data.get('username')
        passw = request.data.get('password')
        
        user = authenticate(username=user, password=passw)
        if not user:
            response = {
            'nouser':None
            }
            return JsonResponse(response)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        profile = 'patient'
        if user.is_superuser:
            profile = 'doctor'
    
        response = {
            'token':token,
            'upk':user.pk,
            'name': user.first_name,
            'admin':user.is_superuser,
            'profile':profile
        }
        return JsonResponse(response)#self.list(request, *args, **kwargs)

class AttendenConsult(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Attend.objects.all()
    serializer_class = AttendSzer

    def get(self, request, *args, **kwargs):
        pk = request.data.get('consultapk',None)
        if pk: 
            self.queryset = Attend.objects.filter(attended_id=pk)

        
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




# CUSTOM VIEWS ---------------------------------------------------------

class newPatient(APIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSzer

    def get(self, request, *args, **kwargs):
        snippets = Patient.objects.all()
        serlializer = PatientSzer(snippets, many=True)
        return Response(serlializer.data)

    def post(self, request, *args, **kwargs):
        serlializer = PatientSzer(data=request.data)
        if serlializer.is_valid():
            serlializer.save()
            data_consulta = {
                'paciente': serlializer.instance.pk,
                'status': 0 
            }
            serlializer_consulta = SingleConsultaSzer(data=data_consulta)
            if serlializer_consulta.is_valid():
                serlializer_consulta.save()
            # assert False,serlializer.instance.pk
            return Response(serlializer_consulta.data, status=status.HTTP_201_CREATED)
        return Response(serlializer.errors)
        #return self.create(request, *args, **kwargs)



class setConsulta(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Consulta.objects.all()
    serializer_class = setConsultaSzer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        obj = self.queryset.get(pk=request.data['consultapk'])
        paciente_info = simplejson.dumps(request.data['patient_info'],True)
        obj.patient = paciente_info
        obj.save()
        return self.list(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

