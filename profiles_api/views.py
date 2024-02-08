from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 

from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        "Return list of APIView features"
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, delete)',
            'Is similar to a tradional Django View',
            'Give you most control over app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Hello with message and name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status =status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request, pk=None):
        """Hande Updating object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Hande partial Updating object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Handle deleting ing object"""
        return Response({'method': 'DELETE'})
