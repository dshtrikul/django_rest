from rest_framework import serializers
from .models import Language, Family, Countries

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'family', 'speakers', 'countries')

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('id', 'url', 'name')

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ('id', 'url', 'name')
