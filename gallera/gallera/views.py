import logging

from rest_framework import views
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from gallera.exceptions import BadRequestFormatException


logger = logging.getLogger(__name__)


class APIView(views.APIView):
    pass


class ServiceView(APIView):
    request_serializer = None
    response_serializer = None
    http_method = None

    # pylint: disable=unused-argument,no-self-use

    def _allowed_methods(self):
        return [
            self.http_method
        ]

    def request_regular_handling(self, request, data, *args, **kwargs):
        # pylint: disable=not-callable
        rqs = self.request_serializer(data=data)
        rqs.is_valid(raise_exception=True)

        request_result = self.process_request(rqs, request)
        if isinstance(request_result, Response):
            return request_result

        response_data, status_code = request_result
        rps = self.response_serializer(response_data)

        return Response(
            rps.data,
            status=status_code,
        )

    def process_request(self, request_serializer_obj, request):
        raise Exception('process_request method not implemented')

    def get(self, request, *args, **kwargs):
        if self.http_method != 'GET':
            return self.http_method_not_allowed(request, *args, **kwargs)

        return self.request_regular_handling(
            request, request.GET, *args, **kwargs
        )

    def post(self, request, *args, **kwargs):
        if self.http_method != 'POST':
            return self.http_method_not_allowed(request, *args, **kwargs)

        body_sample = request.body[:1000]
        try:
            rq_data = request.data
        except ParseError as exc:
            logger.warning(
                'Received invalid data in request body',
                extra=dict(
                    request_body=body_sample,
                    request_meta=request.META,
                ),
            )
            raise BadRequestFormatException(request, exc)
        return self.request_regular_handling(
            request, rq_data, *args, **kwargs
        )
