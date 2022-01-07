from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=300)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    accuracy = serializers.FloatField()

    class Meta:
        model = Person
        fields = ('name','address','latitude','longitude','accuracy')

        #////////////////////////////////////////////////

        