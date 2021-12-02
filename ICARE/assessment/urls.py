from django.urls import path
from .views import assessment

urlpatterns = [
    path('assessment/', assessment.as_view(), name="assessment"),
]