import graphene
from graphene_django import DjangoObjectType
from .models import Hospital,Bed

class HospitalType(DjangoObjectType):
    class Meta:
        model:Hospital
        fields = ('id','name','city','address')

class Query(graphene.ObjectTpe):
    all_hospitals = graphene.List(HospitalType)

schema=graphene.Schema(query=Query)