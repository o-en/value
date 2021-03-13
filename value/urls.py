from django.conf.urls import url
from django.contrib import admin

from company.views.company_info import CompanyInfoListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CompanyInfoListView.as_view(), name='company-info'),
    url(r'^show_info/', CompanyInfoListView.as_view(), name='show-info'),
]
