from rest_framework import serializers
from .models import VotesMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotesMerch
        fields = ('post', 'user', 'count')