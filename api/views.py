from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PokemonSerializer
from pokedex.models import Pokemon
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [TokenHasScope(), IsAuthenticated()]
        return [AllowAny()]


@api_view(['GET'])
def index(request):
    """
    API index view that returns a welcome message.
    """
    return Response({"message": "Welcome to the Pokemon API"})
    