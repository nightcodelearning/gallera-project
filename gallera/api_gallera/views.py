# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from gallera.views import ServiceView
from .serializer import ManyChickenSerializer
from .serializer import ChickenRequestSerializer
from .serializer import ChickenSerializer
from .serializer import RegisterChickenSerializer
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
    response_serializer = RegisterChickenSerializer

    http_method = 'POST'

    def process_request(self, request_serializer_obj, request):
        v = request_serializer_obj.validated_data
        o = Owner.objects.first()
        try:
            print v
            new_chicken = Chick(
                born_date=v['born_date'],
                castador_name=v['castador_name'],
                castador_tag=v['castador_tag'],
                coliseo_tag=v['coliseo_tag'],
                tagger_name=v['tagger_name'],
                weight=v['weight'],
                color=v['color'],
                owner=o,
                image=request.FILES['image'],
            )
            new_chicken.save()

            chicks = Chick.objects.all()

            # return (chicks, status.HTTP_200_OK)
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
    response_serializer = ManyChickenSerializer

    http_method = 'GET'

    def process_request(self, request_serializer_obj, request):
      #  v = request_serializer_obj.validated_data

        try:
            chicks = Chick.objects.all()
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

        chickens = dict(
            chickens=chicks,
        )
        return (chickens, status.HTTP_200_OK)


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
