# Package imports
from rest_framework import serializers

# Shoplocal imports
from slx import models


class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Affiliation
        read_only_fields = ('created_datetime', 'modified_datetime')

class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ask
        read_only_fields = ('created_datetime', 'modified_datetime')

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bid
        read_only_fields = ('created_datetime', 'modified_datetime')

#class FulfillmentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = models.Fulfillment
#        read_only_fields = ('created_datetime', 'modified_datetime')

class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Placement
        read_only_fields = ('created_datetime', 'modified_datetime')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        read_only_fields = ('created_datetime', 'modified_datetime')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
