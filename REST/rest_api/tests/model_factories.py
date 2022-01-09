import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from ..models import *

from random import randint
from random import choice

# TEST FIXTURES
class TaxonomyFactory(factory.django.DjangoModelFactory):
  taxa_id = 53326
  clade = 'E'
  genus = 'Ancylostoma'
  species = 'ceylanicum'
  class Meta:
    model = Taxonomy

class ProteinFamilyFactory(factory.django.DjangoModelFactory):
  domain_id = 'PF00360'
  domain_description = 'Phytochromeregion'
  class Meta:
    model = ProteinFamily

class DomainsFactory(factory.django.DjangoModelFactory):
  pfam_id = factory.SubFactory(ProteinFamilyFactory) 
  taxonomy = factory.SubFactory(TaxonomyFactory) 
  description = "abc"
  start = 1
  stop = 2
  class Meta:
    model = Domains


class ProteinFactory(factory.django.DjangoModelFactory):
  protein_id = 'A0A016S8J7'
  taxonomy = factory.SubFactory(TaxonomyFactory) 
  length = 101
  sequence = 'MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA'
  class Meta:
    model = Protein

class ProteinDomainLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProteinDomainLink

    protein = factory.SubFactory(ProteinFactory)
    domains = factory.SubFactory(DomainsFactory)


class ProteinListFactory(ProteinFactory):
  protein_id = [
    {
        "id": 2,
        "protein_id": "A0A016S8J7"
    },
    {
        "id": 3,
        "protein_id": "A0A016SK08"
    },
    {
        "id": 4,
        "protein_id": "A0A016SLU4"
    },
    {
        "id": 5,
        "protein_id": "A0A016SS41"
    },
    {
        "id": 6,
        "protein_id": "A0A016T911"
    },
    {
        "id": 7,
        "protein_id": "A0A016TEY5"
    },
    {
        "id": 8,
        "protein_id": "A0A016TQ94"
    },
    {
        "id": 9,
        "protein_id": "A0A016TTS1"
    },
    {
        "id": 10,
        "protein_id": "A0A016U0V3"
    },
    {
        "id": 11,
        "protein_id": "A0A016U557"
    },
    {
        "id": 12,
        "protein_id": "A0A016U701"
    },
    {
        "id": 13,
        "protein_id": "A0A016UJ17"
    },
    {
        "id": 14,
        "protein_id": "A0A016USI4"
    },
    {
        "id": 15,
        "protein_id": "A0A016V1B2"
    },
    {
        "id": 16,
        "protein_id": "A0A016V7D3"
    },
    {
        "id": 17,
        "protein_id": "A0A016VK28"
    },
    {
        "id": 18,
        "protein_id": "A0A016W2S6"
    },
    {
        "id": 19,
        "protein_id": "A0A016W9A4"
    },
    {
        "id": 20,
        "protein_id": "A0A016WC87"
    },
    {
        "id": 21,
        "protein_id": "A0A016WF52"
    },
    {
        "id": 22,
        "protein_id": "A0A016WMQ5"
    },
    {
        "id": 23,
        "protein_id": "A0A016WYY3"
    },
    {
        "id": 24,
        "protein_id": "A0A016WZR8"
    },
    {
        "id": 1611,
        "protein_id": "A0A0D6LJF5"
    },
    {
        "id": 1612,
        "protein_id": "A0A0D6LM05"
    },
    {
        "id": 1613,
        "protein_id": "A0A0D6LTY2"
    },
    {
        "id": 1614,
        "protein_id": "A0A0D6LUX2"
    },
    {
        "id": 1615,
        "protein_id": "A0A0D6LX61"
    },
    {
        "id": 1616,
        "protein_id": "A0A0D6M2K0"
    },
    {
        "id": 1617,
        "protein_id": "A0A0D6M3G0"
    },
    {
        "id": 1618,
        "protein_id": "A0A0D6M6X9"
    }]
    
class DomainsListFactory(factory.django.DjangoModelFactory):
    pfam_id = factory.SubFactory(ProteinFamilyFactory) 
    taxonomy = factory.SubFactory(TaxonomyFactory) 
    start = 1
    stop = 2

    class Meta:
        model = Domains
   

        