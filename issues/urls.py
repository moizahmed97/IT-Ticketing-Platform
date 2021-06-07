from django.urls import path 
from .views import IssueListView, IssueCreateView, IssueDetailView, IssueUpdateView, IssueDeleteView

app_name = "issues"

urlpatterns = [
    path('', IssueListView.as_view(), name='issue-list'),
    path('create/', IssueCreateView.as_view(), name='issue-create'),
    path('<int:pk>/', IssueDetailView.as_view(), name="issue-detail"),
    path('<int:pk>/update', IssueUpdateView.as_view(), name="issue-update"),
    path('<int:pk>/delete', IssueDeleteView.as_view(), name="issue-delete")
]