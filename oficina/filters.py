import django_filters
from oficina.models import *

class ProdutoFilter(django_filters.FilterSet):
     
     class Meta:
         model = Produto
         fields = {'categoria': ['exact'], 'nome': ['icontains'], 'quantidade': ['icontains']}


