from django.contrib import admin

# Register your models here.
from company.models.company_info import CompanyInfo

admin.site.register(CompanyInfo)