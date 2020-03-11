from rest_framework import serializers
from webapp.models import Consulta
from webapp.models import Sintom
from webapp.models import Patient
from webapp.models import Medic 
from webapp.models import Attend

from inteligence.models import Isintom, Imeasure
from django.contrib.auth.models import User,Group



class UserSzer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = [
            'pk',
            'first_name',
            'email',
        ]

class MedicSzer(serializers.ModelSerializer):
    class Meta: 
        model = Medic
        fields = [
            'speciality',
            'title',
            'contactinfo',
            'userpk',
        ]

class SingleMeasureSzer(serializers.ModelSerializer):
    class Meta: 
        model = Imeasure
        fields = ['name', 'unit']

class IsintomSzer(serializers.ModelSerializer):
    sintom_measure = serializers.StringRelatedField(many=True)
    class Meta:
        model = Isintom
        fields = [
            'name',
            'icon',
            'sintom_measure'
        ]

class ImeasureSzer(serializers.ModelSerializer):
    #sintom = IsintomSzer(many=True, read_only=True)
    class Meta: 
        model = Imeasure
        fields = [
            'sintom',
            'name',
            'unit',
        ]


'''
    DOCTOR FACE SCREEM
    [ ]

'''

class PatientSzer(serializers.ModelSerializer):
    
    class Meta: 
        model = User
        fields = [
            'pk',
            'first_name',
            'username',
            'email',
        ]

class SintomSzer(serializers.ModelSerializer):
    class Meta: 
        model = Sintom
        fields = [
            'pk',
            'sintoma',
            'intensidad',
            'tipo',
            'zona',
            'causa',
            'consultapk'
        ]

class AttendSzer(serializers.ModelSerializer):
    class Meta: 
        model = Attend
        fields =[
            'attended',
            'consulta_attended',
            'start_date',
            'end_date',
            'diagnostic'
        ]

class ConsultaSzer(serializers.ModelSerializer):
    userapply = PatientSzer(read_only=True)
    sintomlist = SintomSzer(many=True, read_only=True)
    attender = AttendSzer(read_only=True)
    class Meta: 
        model = Consulta
        fields = [
            'pk',
            'attender',
            'userapply',
            'date_start',
            'date_end',
            'status',
            'patient',
            'sintomlist',
        ]



class setConsultaSzer(serializers.ModelSerializer):
    attender = AttendSzer(read_only=True)
    userapply = PatientSzer(read_only=True)
    sintomlist = SintomSzer(many=True, read_only=True)

    class Meta: 
        model = Consulta
        fields = [
            'pk',
            'attender',
            'userapply',
            'date_start',
            'date_end',
            'sintomlist',
            'status',
        ]



class SingleConsultaSzer(serializers.ModelSerializer):
    class Meta: 
        model = Consulta
        fields = [
            'pk',
            'userapply',
            'date_start',
            'status'
        ]

