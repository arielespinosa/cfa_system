from django.db import models
from .nomenclators import Office
from .workers import Worker
from .science import Project


class Object(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    OBJECT_STATUS = (
        ('B', 'Baja'),
        ('EU', 'En uso'),
        ('PB', 'Proceso de baja'),
        ('R', 'Roto'),
    )

    date = models.DateField()
    number = models.CharField(max_length=30)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=OBJECT_STATUS)
    responsible = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True, blank=True)
    x_file = models.BooleanField(default=False)
    accounting_inventory = models.BooleanField(default=True)
    computer_item = models.BooleanField(default=False)
    loan_request = models.FileField(null=True, blank=True)
    loan_letter = models.FileField(null=True, blank=True)
    loan = models.BooleanField(default=False)
    transfer = models.BooleanField(default=False)
    transfer_letter_place = models.FileField(null=True, blank=True)
    transfer_letter_economy = models.FileField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.number

