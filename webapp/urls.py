from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from rest_framework_jwt.views import obtain_jwt_token
from webapp.patient_views import ( MyAppointments, DoctorList, setPatient )

urlpatterns = [
	path('get_user/<int:pk>/', views.getUser.as_view()),
	path('consultas/', views.getConsulta.as_view()),
	path('patients/', views.getPatients.as_view()),
	path('getpatients/<int:pk>/', views.getMyPatients.as_view()),

	path('addsintom/<int:pk>/', views.addSintom.as_view()),
	#path('rmsintom/<int:pk>/', views.rmSintom.as_view()),

	path('medic/<int:pk>/', views.Medicinfo.as_view()),
	path('attend/', views.AttendenConsult.as_view()),
    path('manual_auth/', views.getUser.as_view()),
	path('newpatient/', views.newPatient.as_view()),

	#PATIENT ----------------------------------------------------------------------------

	path('patient/myappointments/', MyAppointments.as_view()),
	path('patient/doctors/<int:consultapk>/', DoctorList.as_view()),
	path('patient/setpatient/<int:consultapk>/', setPatient.as_view()),

	#END PATINET ________________________________________________________________________


	#PATIENT 
	path('setconsulta/', views.setConsulta.as_view()),


]