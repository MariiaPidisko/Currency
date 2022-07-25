from api.serializers import RateSerializer, SourceSerializer

from currency.models import Rate, Source

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from rest_framework_csv.renderers import CSVRenderer

from rest_framework_xml.renderers import XMLRenderer


# class RateView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#
#
# class RateDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, CSVRenderer)


class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, CSVRenderer)
