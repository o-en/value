from rest_framework import generics, serializers
from rest_framework.response import Response

from company.models.company_info import CompanyInfo


class CompanyInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ('id', 'corp_code', 'corp_name')

class CompanyInfoListView(generics.ListAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
