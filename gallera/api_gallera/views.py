# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from gallera.views import ServiceView
from .serializer import ChickenRequestSerializer
from .serializer import ChickenSerializer
from .serializer import EmptySerializer
from .models import Chick
from .models import Owner

from django.http import HttpResponse


class BaseApiView(ServiceView):
  #  permission_classes = (Permissions,)
  #  authentication_classes = []
  pass

class RegisterChickView(BaseApiView):

    request_serializer = ChickenRequestSerializer
    response_serializer = ChickenSerializer

    http_method = 'POST'

    def process_request(self, request_serializer_obj, request):
        v = request_serializer_obj.validated_data
        o = Owner.objects.first()
        try:
            print v
            new_chicks = Chick(
                born_date=v['born_date'],
                castador_name=v['castador_name'],
                castador_tag=v['castador_tag'],
                coliseo_tag=v['coliseo_tag'],
                tagger_name=v['tagger_name'],
                weight=v['weight'],
                color=v['color'],
                owner=o
            )
            new_chicks.save()
            return (new_chicks, status.HTTP_200_OK)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise


class GetChickView(BaseApiView):
    request_serializer = EmptySerializer
    response_serializer = ChickenSerializer

    http_method = 'GET'

    def process_request(self, request_serializer_obj, request):
        v = request_serializer_obj.validated_data

        try:
            chick = Chick.objects.last()
        except Chick.DoesNotExist:
            message = (
                'Cuenta no encontrada para celular: {}'
            ).format(v['phone_number'])
            return Response(
                data=dict(
                    code='NotFound',
                    message=message,
                ),
                status=status.HTTP_404_NOT_FOUND,
            )
        return (chick, status.HTTP_200_OK)

class DeleteChickView(BaseApiView):
    pass