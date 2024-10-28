from django.shortcuts import render, redirect
from pages.models import *

def index(request):
    countries= Country.objects.all()
    services= Service.objects.all()[:3]
    testimonials= Testimonial.objects.all()
    context={
    'countries': countries,
    'services': services,
    'testimonials': testimonials,

    }
    return render(request, 'pages/index.html', context)

def about(request):
    services= Service.objects.all()[:3]
    countries= Country.objects.all()
    context={
    'services': services,
    'countries': countries,
    }
    return render(request, 'pages/aboutus.html', context)


def servicedetails(request, service_title, servicefaq_service):
    services= Service.objects.all()
    single_services= Service.objects.get(slug=service_title)
    faqs= ServiceFaq.objects.get(id=servicefaq_service)
    servicefaqs= ServiceFaq.objects.filter(service__slug=service_title)
    context={
    'single_services': single_services,
    'services': services,
    'faqs': faqs,
    'servicefaqs':servicefaqs,
    }
    return render(request, 'pages/servicedetails.html', context)

def jobvacancies(request, country_name, country_id, vacancy_title, countryfaq_country):
    countries= Country.objects.all()
    single_country= Country.objects.get(slug=country_name)
    
    vacancies= Vacancy.objects.get(id= country_id)
    country_vacancies= Vacancy.objects.filter(country__slug= country_name)
    single_vacancy= Vacancy.objects.get(slug= vacancy_title)

    faqs= CountryFaq.objects.get(id=countryfaq_country)
    countryfaqs= CountryFaq.objects.filter(country__slug=country_name)



    context={
    'countries':countries,
    'single_country':single_country,
    'single_vacancy':single_vacancy,
    'vacancies':vacancies,
    'country_vacancies': country_vacancies,
    'faqs':faqs,
    'countryfaqs': countryfaqs,
    

    }

    return render(request, 'pages/vacancies.html', context)



