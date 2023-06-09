from django.contrib import admin
from .models import Portfolio
# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display= ('name','image','address','contact','email','objective','Skills')
admin.site.register(Portfolio,PortfolioAdmin) #allow admin to insert product and its offers


