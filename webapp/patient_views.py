from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.http import  JsonResponse

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

