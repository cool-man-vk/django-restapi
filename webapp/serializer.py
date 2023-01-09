from rest_framework import serializers 
from .models import *

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo 
        # fields = ['first_name','last_name']
        fields = '__all__'