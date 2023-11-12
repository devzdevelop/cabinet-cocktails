from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from cocktails.models import MixedDrinks


class CocktailSerializer(ModelSerializer):

    class Meta:
        model = MixedDrinks
        fields = ('id', 'name','recipe', 'image',)


class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)