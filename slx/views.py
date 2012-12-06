# Package imports
from json import dumps
from sys import exc_info
from traceback import format_tb
from rest_framework import generics

# Class imports
from datetime import datetime as DateTime
from django.http import HttpResponse

# Shoplocal imports
from slx import models, serializers


def four_o_four_error_view(request):
    return HttpResponse(dumps({}), mimetype = 'application/json')

def five_hundred_error_view(request):
    try:
        type, value, tb = exc_info()

        error = models.Error()
        error.message = '%s: %s' % (type.__name__, value)
        error.stack_trace = str().join(format_tb(tb))
        error.url = request.build_absolute_uri()
        error.datetime = DateTime.now()
        error.save()

    finally:
        return HttpResponse(dumps({}), mimetype = 'application/json')


class AffiliationList(generics.ListCreateAPIView):
    """
    This view presents a list of all the affiliations in the system.
    """
    model = models.Affiliation
    serializer_class = serializers.AffiliationSerializer

class AffiliationInstance(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a instance of one of the affiliation in the system.
    """
    model = models.Affiliation
    serializer_class = serializers.AffiliationSerializer


class AskList(generics.ListCreateAPIView):
    """
    This view presents a list of all the asks in the system.
    """
    model = models.Ask
    serializer_class = serializers.AskSerializer

class AskInstance(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a instance of one of the ask in the system.
    """
    model = models.Ask
    serializer_class = serializers.AskSerializer


class BidList(generics.ListCreateAPIView):
    """
    This view presents a list of all the bids in the system.
    """
    model = models.Bid
    serializer_class = serializers.BidSerializer

class BidInstance(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a instance of one of the bid in the system.
    """
    model = models.Bid
    serializer_class = serializers.BidSerializer


#class FulfillmentList(generics.ListCreateAPIView):
#    """
#    This view presents a list of all the fulfillments in the system.
#    """
#    model = models.Fulfillment
#    serializer_class = serializers.FulfillmentSerializer
#
#class FulfillmentInstance(generics.RetrieveUpdateDestroyAPIView):
#    """
#    This view presents a instance of one of the fulfillment in the system.
#    """
#    model = models.Fulfillment
#    serializer_class = serializers.FulfillmentSerializer


class PlacementList(generics.ListCreateAPIView):
    """
    This view presents a list of all the placements in the system.
    """
    model = models.Placement
    serializer_class = serializers.PlacementSerializer

class PlacementInstance(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a instance of one of the placement in the system.
    """
    model = models.Placement
    serializer_class = serializers.PlacementSerializer


class StatusList(generics.ListAPIView):
    """
    This view presents a list of all the statuses in the system.
    """
    model = models.Status
    serializer_class = serializers.StatusSerializer

class StatusInstance(generics.RetrieveAPIView):
    """
    This view presents a instance of one of the status in the system.
    """
    model = models.Status
    serializer_class = serializers.StatusSerializer


class UnitList(generics.ListCreateAPIView):
    """
    This view presents a list of all the units in the system.
    """
    model = models.Unit
    serializer_class = serializers.UnitSerializer

class UnitInstance(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a instance of one of the unit in the system.
    """
    model = models.Unit
    serializer_class = serializers.UnitSerializer


class UserList(generics.ListCreateAPIView):
    """
    This view presents a list of all the users in the system.
    """
    model = models.User
    serializer_class = serializers.UserSerializer

class UserInstance(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a instance of one of the user in the system.
    """
    model = models.User
    serializer_class = serializers.UserSerializer

