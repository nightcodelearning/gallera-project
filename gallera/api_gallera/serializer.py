from rest_framework import serializers
from .models import Chick
from .models import Owner

class EmptySerializer(serializers.Serializer):
    pass

class ChickenRequestSerializer(serializers.Serializer):
    image = serializers.ImageField(
        required=True,
    )
    owner_name = serializers.CharField(
        required=True,
        max_length=255,
    )
    breeder_plate_number = serializers.CharField(
        required=True,
        max_length=255,
    )
    breeder_name = serializers.CharField(
        required=True,
        max_length=255,
    )
    register_date = serializers.DateTimeField(
        required=True,
    )

    coliseo_plate_number = serializers.CharField(
        required=True,
        max_length=255,
    )
    coliseo_responsible = serializers.CharField(
        required=True,
        max_length=255,
    )
    weight = serializers.DecimalField(
        max_digits=19,
        required=True,
        decimal_places=2,
        min_value=0
    )
    color = serializers.ChoiceField(
        choices=Chick.ALLOWED_COLORS,
        required=True,
    )
    cresta = serializers.ChoiceField(
        choices=Chick.ALLOWED_CRESTA,
        required=True,
    )
    pata = serializers.ChoiceField(
        choices=Chick.ALLOWED_PATA,
        required=True,
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
    class Meta:
        model = Chick
        fields = (
            'token',
            'image_url',
            'owner_id',
            'owner_name',
            'breeder_plate_number',
            'breeder_name',
            'register_date',
            'coliseo_plate_number',
            'coliseo_responsible',
            'weight',
            'weight',
            'color',
            'cresta',
            'pata',
        )

class RegisterChickenSerializer(serializers.Serializer):
    new_chicken = ChickenSerializer()
    chickens = ChickenSerializer(many=True)

class ManyChickenSerializer(serializers.Serializer):
        date_created = serializers.DateTimeField()
        count = serializers.IntegerField()
        chickens = ChickenSerializer(many=True)

class ResponseChickenSerializer(serializers.Serializer):
    response = ManyChickenSerializer(many=True)