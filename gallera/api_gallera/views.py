# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from gallera.views import ServiceView
from .serializer import ManyChickenSerializer
from .serializer import ResponseChickenSerializer
from .serializer import ChickenRequestSerializer
from .serializer import ChickenSerializer
from .serializer import RegisterChickenSerializer
from .serializer import EmptySerializer
from .models import Chick
from .models import Search

from django.db.models import Count
from django.db.models.functions import TruncDate

from .models import Owner

from django.http import HttpResponse


class BaseApiView(ServiceView):
  #  permission_classes = (Permissions,)
  #  authentication_classes = []
  pass

class RegisterChickView(BaseApiView):

    request_serializer = ChickenRequestSerializer
    response_serializer = RegisterChickenSerializer

    http_method = 'POST'

    def process_request(self, request_serializer_obj, request):
        v = request_serializer_obj.validated_data
        try:
            new_chicken = Chick(
                owner_name=v['owner_name'],
                breeder_plate_number=v['breeder_plate_number'],
                breeder_name=v['breeder_name'],
                register_date=v['register_date'],
                coliseo_plate_number=v['coliseo_plate_number'],
                coliseo_responsible=v['coliseo_responsible'],
                weight=v['weight'],
                color=v['color'],
                cresta=v['cresta'],
                pata=v['pata'],
                image=request.FILES['image'],
            )
            new_chicken.save()

            chicks = Chick.objects.all()

        except:
            return Response(
                data=dict(
                    code='Server Error',
                    message=(
                        'Unexpected error: {}'
                    ).format(sys.exc_info()[0]),
                ),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        chickens = dict(
            new_chicken=new_chicken,
            chickens=chicks,
        )
        return (chickens, status.HTTP_200_OK)


class GetChickView(BaseApiView):
    request_serializer = EmptySerializer
    response_serializer = ResponseChickenSerializer

    http_method = 'GET'

    def process_request(self, request_serializer_obj, request):
      #  v = request_serializer_obj.validated_data

        try:
            chickens = Chick.objects.all()
            dates = Search.objects.all()

            res = dict(
                chickens=chickens,
                dates=dates,
            )
            return (res, status.HTTP_200_OK)
        except:
            return Response(
                data=dict(
                    code='Server Error',
                    message=(
                        'Unexpected error: {}'
                    ).format(sys.exc_info()[0]),
                ),
                status=status.HTTP_404_NOT_FOUND,
            )



class DeleteChickView(BaseApiView):
    request_serializer = ChickenSerializer
    response_serializer = ManyChickenSerializer

    http_method = 'POST'

    def process_request(self, request_serializer_obj, request):
        v = request_serializer_obj.validated_data
        try:
            v['chicken'].delete()
           # instance = Chick.objects.get(id=id)
           # instance.delete()
            chicks = Chick.objects.all()
            return (chicks, status.HTTP_200_OK)
        except:
            return Response(
                data=dict(
                    code='Server Error',
                    message=(
                        'Unexpected error: {}'
                    ).format(sys.exc_info()[0]),
                ),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
