from django.urls import path
from pages.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('aboutus/', about, name='aboutus'),
    path('servicedetails/<int:service_id>/<int:sfaqid>', servicedetails, name='servicedetails'),
    path('vacancies/<int:cid>/<int:vacancy_id>/<int:cfaqid>', jobvacancies, name='vacancies'),
]

