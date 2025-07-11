from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from token_auth.serializers import TokenAuthenticationSerializer


class AuthenticateTokenAPIView(APIView):
    serializer_class = TokenAuthenticationSerializer

    def post(self, request, *args, **kwargs):
        context = {'request': request}

        ser = self.serializer_class(data=request.data, context=context)
        ser.is_valid(raise_exception=True)
        user = ser.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'key': token.key,
                'user_id': user.id,
                'time': token.created

            }
        )

class TokenDestroyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)