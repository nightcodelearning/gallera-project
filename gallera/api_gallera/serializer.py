from rest_framework import serializers
from .models import Chick
from .models import Owner

class EmptySerializer(serializers.Serializer):
    pass

class ChickenRequestSerializer(serializers.Serializer):
    born_date = serializers.DateTimeField()
    castador_tag = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        default='',
    )

    castador_name = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        default='',
    )

    coliseo_tag = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        default='',
    )

    tagger_name = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        default='',
    )

    weight = serializers.DecimalField(
        max_digits=19,
        decimal_places=2,
        min_value=0
    )

    color = serializers.ChoiceField(
        choices=Chick.ALLOWED_COLORS,
        required=False,
        allow_blank=True,
        default='',
    )


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = (
            'token',
            'legal_id_type',
            'legal_id_number',
            'full_name',
            'email',
        )

class ChickenSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Chick
        fields = (
            'token',
            'born_date',
            'castador_tag',
            'castador_name',
            'born_date',
            'coliseo_tag',
            'tagger_name',
            'weight',
            'color',
            'owner',
        )