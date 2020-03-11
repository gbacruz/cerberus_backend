from django.db import models
from django.contrib.auth.models import User,Group
import simplejson

class Medic(models.Model):
    userpk = models.ForeignKey(User, related_name='medic_user', on_delete=models.CASCADE)
    speciality = models.TextField()
    title = models.TextField()
    contactinfo = models.TextField()
    location = models.TextField(blank=True,null=True)
    keywords = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.userpk.username


class MedicSym(models.Model):
    medico = models.ForeignKey(Medic, on_delete=models.CASCADE)
    symptom = models.CharField(u'sym', max_length=500, default="dolor")
    level = models.IntegerField(default=20)


class Patient(models.Model):
    userpk = models.ForeignKey(User, related_name='user_general', on_delete=models.CASCADE)
    age = models.IntegerField()
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=(('m', 'Masculino'),('f', 'Femenino')))

class HealthInfo(models.Model):
    userpk = models.ForeignKey(Patient, related_name='user_health', on_delete=models.CASCADE)
    elemento = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=(
        ('allergie', 'Alergia'),
        ('cronic', 'Cronic'),
        ('indication', 'Indication')
        )
    )

class Consulta(models.Model):
    userapply = models.ForeignKey(User, related_name='pacientepk', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10)
    patient = models.TextField(blank=True, null=True)

    def patient_name(self):
        paciente = simplejson.loads(self.patient)
        return paciente['name']

class Sintom(models.Model):
    consultapk = models.ForeignKey(Consulta, related_name='sintomlist', on_delete=models.CASCADE)
    sintoma = models.TextField()
    intensidad = models.CharField(max_length=120,blank=True, null=True)
    tipo = models.CharField(max_length=120,blank=True, null=True)
    zona = models.TextField(blank=True, null=True)
    causa = models.TextField(default='unknow', blank=True, null=True)

class Attend(models.Model):
    attended = models.ForeignKey(User, related_name='attender', on_delete=None)
    consulta_attended = models.ForeignKey(Consulta, related_name='consulta_atendida', on_delete=models.CASCADE)
    diagnostic = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
class Medication(models.Model):
    attender = models.ForeignKey(Attend, related_name='attend_medication', on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=200)
    cuantity = models.CharField(max_length=200)
    regularity = models.CharField(max_length=100)
    temporarity = models.CharField(max_length=100)
    
