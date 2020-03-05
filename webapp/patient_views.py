from django.contrib.auth.models import User
from django.views import View
from django.http import  JsonResponse
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import simplejson
from webapp.models import (Medic, Consulta)
'''
    HERE, you could add elements of a navigation structure, divides into:
    MAINSECTION (as usual, not navegable mode)
    COLUMNS, a division on to menu area
    section, the navegable page

'''


class MyAppointments(View):

    def get(self, request, *args, **kwargs):
    
        appointments = [
            {
                'patient':{
                    'name':'Juan',
                    'age':'9',
                    'gender':'Masculino',
                    'status':''
                },
                'symptoms':[
                    {'name':'obstrucción',
                     'zone':'oido',
                     'intensity':''
                    },
                ],
                'info':{
                    'location':'2 km'
                },
                'signals':[]
            },
            {
                'patient':{
                    'name':'Matti',
                    'age':'29',
                    'gender':'Femenino',
                    'status':''
                },
                'symptoms':[
                    {'name':'dolor',
                     'zone':'cabeza',
                     'intensity':'intenso'
                    },
                    {'name':'Temperatura',
                     'zone':'',
                     'intensity':'alta'
                    },
                ],
                'info':{
                    'location':'16 km'
                },
                'signals':[
                    {'name':'Temperatura',
                     'metrica':'79 grados centigrados',
                     'temporalidad':'40 minutos'
                    }
                ]
            }

        ]
        return JsonResponse(appointments, safe=False)#self.list(request, *args, **kwargs)

class Inteligence:
    SPECIAL = [u'Cardiólogo',u'Pediatra',u'Neurólogo',u'Ortopedista','Medicina General','Psicología','Psiquiatría']

    specialities = {
            'dolor-cabeza':'Medicina General',
            'dolor-corazon':'Cardiólogo',
            'vomito':'Medicina General',
            'diarrea':'Medicina General',
            'contractura':'Ortopedista',
            'depresion':'Psicología',
            'violencia':'Psicología',
            'dolor-cuerpo':'Medicina General',
        }

class DoctorList(View,Inteligence):
    def get(self, request, consultapk=None, *args, **kwargs):
        c = Consulta.objects.get(pk=consultapk)
        specialkwords = ['%s-%s'%(x.sintoma, x.zona) for x in c.sintomlist.all()]
        spk = []
        for x in list(set(specialkwords)):                
            try: 
                p = self.specialities[x]
                spk.append(p)
            except:
                next


        doctors_list = [
            {'speciality':medic.speciality,
             'title':medic.title,
             'name':'%s %s'%(medic.userpk.first_name, medic.userpk.last_name )
             
            }
            for medic in Medic.objects.filter(speciality__in=spk)
        ]
        return JsonResponse(doctors_list, safe=False)

class setPatient(View,Inteligence):
    def post(self, request, consultapk=None, *args, **kwargs):
        c = Consulta.objects.get(pk=consultapk)
        patientinfo = request.POST.get('patient_info')
        c.patient = patientinfo 
        assert False,patientinfo
        return JsonResponse({'done':True}, safe=False)

