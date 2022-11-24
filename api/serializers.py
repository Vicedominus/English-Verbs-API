from rest_framework.serializers import ModelSerializer

from .models import Verb


class VerbSerializer(ModelSerializer):

    class Meta:
        model = Verb
        fields = '__all__'