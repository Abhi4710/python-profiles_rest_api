from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """returns a list of API view features"""
        an_apiview = [
            'Uses Http methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'GIves you the most control over your application logic',
            'Is mapped manually to Urls'
        ]

        return Response({'message': 'Hello!',
                         'an_apiview': an_apiview})