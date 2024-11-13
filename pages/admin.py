from django.contrib import admin
from pages.models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Testimonial)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('sid', 'title', 'is_active')
	list_display_links = ('sid', 'title')
# Register your models here.
admin.site.register(Service, ServiceAdmin)

class ServiceFaqAdmin(admin.ModelAdmin):
	list_display = ('sfaqid', 'service')
	list_display_links = ('sfaqid', 'service')
# Register your models here.
admin.site.register(ServiceFaq, ServiceFaqAdmin)

class CountryAdmin(admin.ModelAdmin):
	list_display = ('cid', 'name')
	list_display_links = ('cid', 'name')
# Register your models here.
admin.site.register(Country, CountryAdmin)

class CountryFaqAdmin(admin.ModelAdmin):
	list_display = ('cfaqid', 'country', 'question')
	list_display_links = ('cfaqid', 'country', 'question')
# Register your models here.
admin.site.register(CountryFaq, CountryFaqAdmin)

class VacancyAdmin(admin.ModelAdmin):
	list_display = ('vid', 'title')
	list_display_links = ('vid', 'title')
# Register your models here.
admin.site.register(Vacancy, VacancyAdmin)