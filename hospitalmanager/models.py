from django.db import models

# Create your models here.
from django.db import models


class Hospital(models.Model):
    id = models.CharField(max_length='10')
    name = models.CharField(max_length='50')
    city = models.CharField(max_length='20')
    address = models.CharField(max_length='100')

    def __str__(self):
        return self.name


class Bed(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    bedNumber = models.CharField(max_length='10')
    TYPE_OF_BEDS = [
        ('GEN', 'General'),
        ('QUA', 'Quarantine'),
        ('ICU', 'Intensive Care Unit (ICU)'),
        ('FOW', 'Fowler'),
        ('SFOW', 'Semi Fowler'),
        ('ELE', 'Electric'),
    ]
    bedType = models.CharField(
        max_length='3',
        choices=TYPE_OF_BEDS,
        default='GEN'
    )
    is_single = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hospital} {self.bedNumber} {self.bedType}"
