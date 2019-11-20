from rest_framework.serializers import ModelSerializer
from .models import PublicationHouse

class PublicationHouseSerializer(ModelSerializer):
  class Meta:
    model = PublicationHouse
    fields = ('id', 'name', 'ratings')