from __future__ import unicode_literals
from django import forms
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Hidrometros(models.Model):
    local = models.CharField(max_length=45)
    medicao_inicial = models.FloatField(blank=True, null=True)
    medicao_final = models.FloatField(blank=True, null=True)
    horario_ligamento = models.TimeField(blank=True, null=True)
    horario_desligamento = models.TimeField(blank=True, null=True)
    data = models.DateField()

    class Meta:
        db_table = 'hidrometros'

    def get_absolute_url(self):
        return reverse("hidrometros:detail", kwargs={"id": self.id})

    def consumo_diurno(self):
        if self.medicao_inicial==None or self.medicao_final==None:
            return "Aguardando Dados"
        else:
            return (self.medicao_final - self.medicao_inicial)

# class Posts(models.Model):
#     title = models.CharField(max_length=45, blank=False, null=False)
#     content = models.CharField(max_length=45, blank=False, null=False)
#     updated = models.DateTimeField(blank=True, null=True)
#     timestamp = models.DateTimeField(blank=True, null=True)
#     data = models.DateField(blank=False, null=False)

#     def __unicode__(self):
#         return self.title

#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={"id": self.id})

#     class Meta:
#         #managed = False
#         db_table = 'posts'