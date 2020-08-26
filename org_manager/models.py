from django.db import models

# Create your models here.
class Manager(models.Model):

    first_name = models.CharField(max_length=100, null=True,  blank=True)
    last_name = models.CharField(max_length=100, null=True,  blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250, blank=False, null=False)
    address = models.TextField(blank=True, null=True, unique=False)
    dob = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=250, blank=True, null=True, default=None)

    @property
    def representation(self):
        return 'Name: {}'.format(self.email)

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

    def __str__(self):
        return self.representation


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True,  blank=True)
    last_name = models.CharField(max_length=100, null=True,  blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250, blank=False, null=False)
    address = models.TextField(blank=True, null=True, unique=False)
    dob = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=250, blank=True, null=True, default=None)
    mobile = models.CharField(max_length=10, blank=True, null=True, default=None)

    @property
    def representation(self):
        return 'Name: {}'.format(self.email)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __str__(self):
        return self.representation