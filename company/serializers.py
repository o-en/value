from rest_framework import serializers

from company.models.company_info import CompanyInfo


class CompanyInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ('id', 'corp_code', 'corp_name')