from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inteligence import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
	path('isintom/', views.IsintomV.as_view()),
	path('measure/', views.MeasureV.as_view()),


]