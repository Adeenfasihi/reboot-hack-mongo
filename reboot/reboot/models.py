from django.db import models

class SME(models.Model):
    sme_id = models.IntegerField()
    sme_name = models.CharField(max_length=25)
    sme_email = models.CharField(max_length=25)
    sme_password = models.CharField(max_length=25)
    sme_postcode = models.CharField(max_length=8)
    sme_industry = models.CharField(max_length=25)
    sme_sector = models.CharField(max_length=25)
    sme_network = models.CharField(max_length=200)

class Supplier(models.Model):
    supplier_id = models.IntegerField()
    supplier_name = models.CharField(max_length=25)
    supplier_email = models.CharField(max_length=25)
    supplier_password = models.CharField(max_length=25)
    supplier_postcode = models.CharField(max_length=8)
    supplier_industry = models.CharField(max_length=25)
    supplier_sector = models.CharField(max_length=25)