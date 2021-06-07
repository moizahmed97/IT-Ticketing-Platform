from issues.views import LandingPageView,SignUpView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('issues/', include('issues.urls', namespace="issues")), # Forward all /issues urls to the issues app urls file
    path('technicians/', include('technicians.urls', namespace="technicians")), # Forward all /technicians urls to the issues app urls file
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup', SignUpView.as_view(), name='signup')
]
