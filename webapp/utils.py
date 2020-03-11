from webapp.models import *
from django.contrib.auth.models import * 


SPECIAL = [u'Cardiólogo',u'Pediatra',u'Neurólogo',u'Ortopedista','Medicina General','Psicología','Psiquiatría']


def fills():
    for x in range(0,7):
        for y in range(100,110):
            user = {
                'username':'username_%s_%s'%(x,y),
                'password':'e4$%s'%(y),
                'email':'username_%s_%s@mail.com'%(x,y),
                'is_superuser':True
            }
            print(user)
            u = User.objects.create_user(username=user['username'],
                                 email=user['email'],
                                 password=user['password'])
            medic = {
                'userpk':u,
                'speciality':SPECIAL[x],
                'title':SPECIAL[x],
                'contactinfo':[],
                'location':x
            }


            m = Medic(**medic)
            m.save()
    

class Intelligence:
    LEVEL_ONE = ['Pediatric','General','Geriatric']
    LEVEL_ZONE = ['cardio','neuro','gastro','ortopedic','dentist','otorino','','','','','']

    def level_one(self):
        if 0 <= self.patient.age <=10:
            LEVEL_ONE = {
                'level':LEVEL_ONE[0],
                'percent':100
            }
        if 10 <= self.patient.age <=14:
            LEVEL_ONE = [
                {
                'level':LEVEL_ONE[0],
                'percent':50
                },
                {
                'level':LEVEL_ONE[1],
                'percent':50
                },
            ]
        if 14 <= self.patient.age <=45:
            LEVEL_ONE = {
                'level':LEVEL_ONE[1],
                'percent':100
            }
        if  self.patient.age > 45:
            LEVEL_ONE = {
                'level':LEVEL_ONE[2],
                'percent':100
            }

    def level_zone(self):
        for x in self.symmtoms:
            sym = x.sintoma
            zone = x.zona
        if zone:
            
