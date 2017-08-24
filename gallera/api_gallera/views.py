# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# comentario

from gellera.views import ServiceView
from .serializer import ChickenRequestSerializer
from .serializer import ChickenSerializer


class BaseApiView(ServiceView):
  #  permission_classes = (Permissions,)
  #  authentication_classes = []
  pass

class RegisterChickView(BaseApiView):
    request_serializer = ChickenRequestSerializer
    response_serializer = ChickenSerializer

    http_method = 'GET'

    def process_request(self, request_serializer_obj, request):
        v = request_serializer_obj.validated_data

        try:
            account = Account.objects.get(phone_number=v['phone_number'])
        except Account.DoesNotExist:
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
        return (account, status.HTTP_200_OK)

class GetChickView(BaseApiView):
    pass

class DeleteChickView(BaseApiView):
    pass