from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AdminAndLoginRequiredMixin(AccessMixin):
    """  Check if the user is authenticated and admin or not
         Use this mixin in views which we only want the admin to access eg Delete Agents    
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)
