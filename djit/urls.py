from issues.views import LandingPageView,SignUpView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('issues/', include('issues.urls', namespace="issues")), # Forward all /issues urls to the issues app urls file
    path('technicians/', include('technicians.urls', namespace="technicians")), # Forward all /technicians urls to the issues app urls file
    path('issuers/', include('issuers.urls', namespace="issuers")), # Forward all /issuers urls to the issues app urls file
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('reset-password', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done', PasswordResetDoneView.as_view(), name='password_reset_done'), # The name has to be this as Django expects it 
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), # The name has to be this as Django expects it 
    path('password-reset-complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'), # The name has to be this as Django expects it 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)