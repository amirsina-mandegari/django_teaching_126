from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailBackend(BaseBackend):
    """Authenticate using email instead of username"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None
        try:
            user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        
        
