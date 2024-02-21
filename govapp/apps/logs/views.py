from drf_spectacular import utils as drf_utils
from rest_framework import viewsets

from govapp.apps.logs import models, serializers


@drf_utils.extend_schema(tags=["Logs - Communications Logs"])
class CommunicationsLogEntryViewSet(viewsets.ModelViewSet):
    """Communications Log Entry View Set."""

    queryset = models.CommunicationsLogEntry.objects.all()
    serializer_class = serializers.CommunicationsLogEntrySerializer
    filterset_fields = ["content_type", "object_id"]


@drf_utils.extend_schema(tags=["Logs - Action Logs"])
class ActionsLogEntryViewSet(viewsets.ModelViewSet):
    """Actions Log Entry View Set."""

    queryset = models.ActionsLogEntry.objects.all()
    serializer_class = serializers.ActionsLogEntrySerializer
    filterset_fields = ["content_type", "object_id"]
