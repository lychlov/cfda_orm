from django.db import models


# Create your models here.

class Source(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    ik = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.id


class Information(models.Model):
    regist_id = models.CharField(max_length=200)
    enterprise_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    notify_time = models.DateTimeField()
    reseive_date = models.CharField(max_length=200)
    fee_status = models.CharField(max_length=200)
    fee_date = models.DateField()
    test_date = models.DateField()
    classify = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    crawl_time = models.DateTimeField()

    def __str__(self):
        return self.regist_id + ":" + self.enterprise_name
