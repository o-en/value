from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from company.models.company_info import CompanyInfo
from company.serializers import CompanyInfoListSerializer


class CompanyInfoListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'company/company_list.html'

    def get(self, request):
        serializer = CompanyInfoListSerializer(data=request.data)
        return Response({'companys': []})
    
    def post(self, request):
        company_name = request.POST.get('company-name')

        return Response({'companys': CompanyInfo.objects.filter(corp_name__contains=company_name)})
