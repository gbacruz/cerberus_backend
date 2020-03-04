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
    