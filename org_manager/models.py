from django.db import models

# Create your models here.
class Manager(models.Model):

    first_name = models.CharField(max_length=100, null=True,  blank=True)
    last_name = models.CharField(max_length=100, null=True,  blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250,blank=False,null=False)
    address = models.TextField(blank=True,null=True,unique=False)
    dob = models.DateField(null=False, blank=False)
    company = models.TextField(blank=True,null=True,unique=False)

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
    password = models.CharField(max_length=250,blank=Falsenull=False)
    address = models.TextField(blank=Truenull=True,unique=False)
    dob = models.DateField(null=False, blank=False)
    company = models.TextField(blank=True,null=True,unique=False)
    mobile = models.IntegerField(null=False, blank=False)

    @property
    def representation(self):
        return 'Name: {}'.format(self.email)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __str__(self):
        return self.representation