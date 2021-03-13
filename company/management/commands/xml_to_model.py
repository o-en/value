from xml.etree import ElementTree

from django.core.management.base import BaseCommand

from company.models import CompanyInfo


class Command(BaseCommand):
    def handle(self, *args, **options):
        tree = ElementTree.parse('CORPCODE.xml')
        root = tree.getroot()

        for corp_code, corp_name in zip(root.iter("corp_code"), root.iter("corp_name")):
            CompanyInfo.objects.create(corp_code=corp_code.text, corp_name=corp_name.text)