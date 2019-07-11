from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Family, Countries
from .serializers import LanguageSerializer, FamilySerializer, CountrySerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# Create your views here.

class FamilyView(viewsets.ModelViewSet):
    queryset= Family.objects.all()
    serializer_class = FamilySerializer
    # permission_classes = (permissions.IsAuthenticated,)

class CountryView(viewsets.ModelViewSet):
    queryset= Countries.objects.all()
    serializer_class = CountrySerializer
