from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializer import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from .models import UserProfile, ProfileFeedItem
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from .permissions import UpdateOwnProfile, UpdateOwnStatus
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = HelloSerializer

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

    def post(self, request):
        """create a hello msg with the name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating objects"""
        return Response({
            'method': 'put'
        })

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({
            'method': 'patch'
        })

    def delete(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({
            'method': 'delete'
        })


class HelloViewSet(viewsets.ModelViewSet):
    """Test API Viewset"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = {
            'Users action (list, create, update, delete, partial_update)',
            'Automatically maps to URLS using routers',
            'Provides more function with less code'
        }

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating users profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    pass


class UserLoginApiView(ObtainAuthToken):
    """Handle creatig user authentication token"""
    """DEFAULT_RENDERER_CLASSES adds the renderer class to our obtain auth view. other views has this by default"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSets(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feedd items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProfileFeedItemSerializer
    permission_classes = (UpdateOwnStatus, IsAuthenticated, )
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        """customize the logic to save an object field can use perform_create"""
        serializer.save(user_profile=self.request.user)
