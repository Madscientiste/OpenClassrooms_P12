import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

logger = logging.getLogger(__name__)


@api_view()
def handle_login(request):
    logger.info("AYAYA")
    return Response({"message": "AYAYA technologies !!"})


@api_view()
def handle_logout(request):
    logger.info("AYAYA 2")
    return Response({"message": "AYAYA technologies !!"})
