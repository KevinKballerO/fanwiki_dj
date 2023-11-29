from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Character
from.models import Episodes
from .serializers import CharacterSerializer
from.serializers import EpisodesSerializaer
#from django.contrib.auth.models import User #usuario
#from .serializers import UserSerializer #usuario

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
   
    def list(self, request):
       name = request.query_params.get('name', None)
       status = request.query_params.get('status', None)
       species = request.query_params.get('species', None)

       queryset = Character.objects.all()

       if name:
           queryset = queryset.filter(name__icontains=name)
       if status:
           queryset = queryset.filter(status=status)
       if species:
           queryset = queryset.filter(species=species)

       serializer = CharacterSerializer(queryset, many=True)
       return Response(serializer.data)


class EpisodesViewSet(viewsets.ModelViewSet):
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializaer

#class UserViewSet(viewsets.ModelViewSet): #para el usuario
 #  queryset = User.objects.all()
  # serializer_class = UserSerializer    

#def signup(request):
 #   if request.POST['password']:
  #      try:
   #3         user = User.objects.create_user(username=request.POST[' username'],
    #        password =  request.POST['password'])
     #       user.save()
      #      return HttpResponse('User created')
       # except:
        #    return HttpResponse('User name exists')
        #return  HttpResponse('Password do not match')
                                                                       
                                            
