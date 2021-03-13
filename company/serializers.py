import requests
import json

from django.conf import settings
from rest_framework import serializers

from company.models.company_info import CompanyInfo


class CompanyInfoListSerializer(serializers.ModelSerializer):
    dividend = serializers.SerializerMethodField()
    class Meta:
        model = CompanyInfo
        fields = ('id', 'corp_code', 'corp_name', 'dividend')


    def get_dividend(self, obj):
        params = {
            'crtfc_key': settings.CRTFC_KEY,
            'corp_code': obj.corp_code,
            'bsns_year': 2019,
            'reprt_code': 11011
        }
        r = requests.get(
            url='https://opendart.fss.or.kr/api/alotMatter.json',
            params=params
        )
        d_list = json.loads(r.text).get('list')
        if d_list:
            return d_list[4].get('thstrm')
        return '2019년 정보가 존재하지 않습니다.'