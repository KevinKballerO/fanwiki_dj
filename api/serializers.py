from rest_framework import serializers
from .models import Character
from .models import Episodes

# from django.contrib.auth.models import User #importar el usuario


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class EpisodesSerializaer(serializers.ModelSerializer):
    # characters = serializers.PrimaryKeyRelatedField(many=True, queryset=Character.objects.all())
    characters = CharacterSerializer(many=True)
    #characters = serializers.SerializerMethodField()

    class Meta:
        model = Episodes
        fields = "__all__"
    
    #def get_characters(self, episode):
    #    characters = episode.characters.all()
     #  return [character.get_absolute_url() for character in characters]

# class UserSerializer(serializers.ModelSerializer): #usuario
#  class Meta:
#     model = User
#    fields = ['id', 'username', 'email', 'is_active', 'created', 'updated']
#   read_only_field = ['is_active', 'created', 'updated']
