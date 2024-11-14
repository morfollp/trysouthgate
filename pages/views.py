from django.shortcuts import render, redirect
from pages.models import *
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



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


def servicedetails(request, service_id, sfaqid):
    services= Service.objects.all()
    single_services= Service.objects.get(sid=service_id)
    faqs= ServiceFaq.objects.get(sfaqid=sfaqid)
    servicefaqs= ServiceFaq.objects.filter(service__sid=service_id)
    context={
    'single_services': single_services,
    'services': services,
    'faqs': faqs,
    'servicefaqs':servicefaqs,
    }
    return render(request, 'pages/servicedetails.html', context)

def jobvacancies(request, cid, vacancy_id, cfaqid):
    countries= Country.objects.all()
    single_country= Country.objects.get(cid=cid)
    
    vacancies= Vacancy.objects.get(vid=vacancy_id)
    country_vacancies= Vacancy.objects.filter(country__cid= cid) 

    faqs= CountryFaq.objects.get(cfaqid=cfaqid)
    countryfaqs= CountryFaq.objects.filter(country__cid=cid)



    context={
    'countries':countries,
    'single_country':single_country,
    'vacancies':vacancies,
    'country_vacancies': country_vacancies,
    'faqs':faqs,
    'countryfaqs': countryfaqs,
   'vacancy_url': reverse('vacancies', args=[vacancies.country.cid, vacancies.vid, faqs.cfaqid]),
    

    }

    return render(request, 'pages/vacancies.html', context)


def contact(request):
    if request.method == "POST":
        contact=Contact()
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        subject= request.POST.get('subject')
        description= request.POST.get('description')

        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.subject=subject
        contact.description=description
        contact.save()
        # Send contact to info@southgateimmigration
        # mail_subject = 'Someone Messaged You!'
        # message= name+'has messaged you. Email:'+email+'Phone:'+phone+'Subject:'+subject+'Message:'+ description
        # send_email = EmailMessage(mail_subject, message, to=['neerajjpgvr@gmail.com'])
        # send_email.send()
        return HttpResponse('<h1>Thanks for contacting us</h1>')
    return render(request, 'pages/contact.html', {})



