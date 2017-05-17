from database.models import GliaUser
from rest_framework import authentication
from rest_framework import exceptions

class GliaAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        gliaId = request.META.get('HTTP_GLIAID')
        
        if request.method == "GET":
            return None
        
        try:
            user = GliaUser.objects.get(gliaID=gliaId)
        except GliaUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('You do not have the necessary permissions')
        return (user, None)