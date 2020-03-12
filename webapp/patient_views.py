from django.contrib.auth.models import User
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.views import View
from django.http import  JsonResponse
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import simplejson
from webapp.models import *
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



class DoctorList(View):
    def get(self, request, consultapk=None, *args, **kwargs):
        c = Consulta.objects.get(pk=consultapk)
        qs = Q()
        medicos = []
        sintoms = [slugify(x.sintoma) for x in c.sintomlist.all()]
        for x in sintoms:
            qs |= Q(names__icontains=x)

        print(qs)
        if len(qs)==0:
            return JsonResponse(medicos, safe=False)

        pred = Prediagnostic.objects.filter(qs).distinct()
        for p in pred:
            diagnosis = p.special.all().distinct()
            for d in diagnosis:
                
                for m in d.specialmedic_set.all().distinct():
                    med = {'speciality':m.special.speciality,
                        'title':m.medicpk.title,
                        'name':'%s %s'%(m.medicpk.userpk.first_name, m.medicpk.userpk.last_name),
                        'medic_pk':m.medicpk.userpk.id
                        }

                    medicos.append(med)    
        return JsonResponse(medicos, safe=False)

class setPatient(View):
    def post(self, request, consultapk=None, *args, **kwargs):
        c = Consulta.objects.get(pk=consultapk)
        patientinfo = request.POST.get('patient_info')
        c.patient = patientinfo 
        assert False,patientinfo
        return JsonResponse({'done':True}, safe=False)

