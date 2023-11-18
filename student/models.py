from django.db import models
from base.models import BaseModel

class Tier(BaseModel):
    tier = models.CharField(max_length=10)
    def __str__(self):
        return self.tier

class Student(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    Tier = models.ForeignKey(Tier, on_delete=models.CASCADE, related_name='Tier')
    completed_gen_ai = models.BooleanField(default=True)
    pathwaycompleted = models.BooleanField(default=False)
    dateofCompletion = models.DateField()
    eligible_for_certificate = models.BooleanField(default=True)
    sized_entered = models.BooleanField(default=False)
    size=models.CharField(max_length=1, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

