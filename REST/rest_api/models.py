from typing import Sequence
from django.db import models

# Create your models here.
class Taxonomy(models.Model):
  taxa_id = models.IntegerField(null=False, blank=False, primary_key=True)
  clade = models.CharField(max_length=256, null=False, blank=False)
  genus = models.CharField(max_length=256, null=False, blank=False)
  species = models.CharField(max_length=256, null=False, blank=False)
  def __str__(self):
    return self.clade
  def __str__(self):
    return self.genus
  def __str__(self):
    return self.species

class ProteinFamily(models.Model):
  domain_id =  models.CharField(max_length=256, null=False, blank=False, primary_key=True)
  domain_description = models.CharField(max_length=256, null=False, blank=False)
  # return a strings
  def __str__(self):
    return self.domain_description
  def __str__(self):
    return self.domain_id



class Protein(models.Model):
  protein_id = models.CharField(max_length=256, null=False, blank=False, primary_key=True) # removed primarykey=true
  taxonomy = models.ForeignKey(Taxonomy, on_delete=models.DO_NOTHING)
  length = models.IntegerField(null=False, blank=False)
  # protein_family = models.ForeignKey(ProteinFamily, on_delete=models.DO_NOTHING)
  # sequence =  models.ForeignKey(Sequence, on_delete=models.DO_NOTHING, blank=True, null=True)

 
  #fk_protein_family = models.ForeignKey(ProteinFamily, on_delete=models.DO_NOTHING)
  # fk_sequence = models.ForeignKey(Sequence, on_delete=models.DO_NOTHING)
   # return a strings
  def __str__(self):
    return self.protein_id
 

class Domains(models.Model):
  pfam_id = models.ForeignKey(ProteinFamily, on_delete=models.DO_NOTHING)
  taxonomy = models.ForeignKey(Taxonomy, on_delete=models.DO_NOTHING)
  protein = models.ForeignKey(Protein, on_delete=models.DO_NOTHING)
  description = models.CharField(max_length=500, null=False, blank=False)
  start = models.IntegerField(null=False, blank=False)
  stop = models.IntegerField(null=False, blank=False)

  def __str__(self):
    return self.protein
  def __str__(self):
    return self.description
  def __str__(self):
    return str(self.pfam_id)
  
 


#https://www.sankalpjonna.com/learn-django/representing-foreign-key-values-in-django-serializers