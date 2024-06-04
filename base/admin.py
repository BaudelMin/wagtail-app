from django.contrib import admin
from .models import NavigationSettings, FooterText
# Register your models here.
admin.site.register(NavigationSettings)
admin.site.register(FooterText)