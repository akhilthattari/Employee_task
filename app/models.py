from django.db import models

class Employee(models.Model):
    WORK_STATUS_CHOICES = (
        ('WFO', 'Work From Office'),
        ('WFH', 'Work From Home'),
    )

    name = models.CharField(max_length=100)
    work_status = models.CharField(max_length=3, choices=WORK_STATUS_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50, blank=True, null=True)
   

    def __str__(self):
        return self.name
