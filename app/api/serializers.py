from currency.models import Rate, Source

from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
            'created',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'contact_number',
        )
