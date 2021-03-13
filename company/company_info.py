from django.db import models


class CompanyInfo(models.Model):
    corp_code = models.CharField(max_length=20)
    corp_name = models.CharField(max_length=200)


    def __str__(self):
        return self.corp_name