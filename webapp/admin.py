from django.contrib import admin
from webapp.models import (Medic, MedicSym,
                            Prediagnostic, Specialist,
                            SpecialMedic
                            )

admin.site.register(Medic)
admin.site.register(MedicSym)
admin.site.register(Prediagnostic)
admin.site.register(Specialist)
admin.site.register(SpecialMedic)

# Register your models here.
