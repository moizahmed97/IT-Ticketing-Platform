from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AdminAndLoginRequiredMixin(AccessMixin):
    """  Check if the user is authenticated and admin or not
         Use this mixin in views which we only want the admin to access eg Delete Agents    
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect("issues:issue-list")
        return super().dispatch(request, *args, **kwargs)


class AdminAndIssuerMixin(AccessMixin):
    """  Check if the user is authenticated and if they are admin or a issuer
         Use this mixin for CRUD of things that an issuer or admin can do 
         like Create Update and Delete issues     
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_technician:
            return redirect("issues:issue-list")
        return super().dispatch(request, *args, **kwargs)

