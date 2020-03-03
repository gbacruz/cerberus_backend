from django.db import models
from jsonfield import JSONField

class Isintom(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200, blank=True, null=True)

class Imeasure(models.Model):
    sintom = models.ForeignKey(Isintom, related_name='sintom_measure', on_delete=None)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return '%d: %s' % (self.pk, self.name)


class Izone(models.Model):
    part = models.CharField(max_length=200)
    icon = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('Izone', related_name='parent_zone', on_delete=None)

'''
este modelo potencializara 
'''
class Ipotential(models.Model):
    minlimit = models.IntegerField()
    maxlimit = models.IntegerField()
    potential = models.IntegerField()
    isintompk = models.ForeignKey(Isintom,related_name='isintompk',on_delete=None)