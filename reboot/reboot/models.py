from django.db import models

class SME(models.Model):
    sme_name = models.CharField(max_length=25)
    sme_email = models.CharField(max_length=25)
    sme_password = models.CharField(max_length=25)
    sme_postcode = models.CharField(max_length=8)
    sme_industry = models.CharField(max_length=25)
    sme_sector = models.CharField(max_length=25)
