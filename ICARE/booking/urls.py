from django.urls import path
from .views import pbookapt, dmanageapt, dviewapt
from account import urls

urlpatterns = [
    path("pbookapt/", pbookapt.as_view(), name="pbookapt"),
    path("dmanageapt/", dmanageapt.as_view(), name="dmanageapt"),
    path("dviewapt/", dviewapt.as_view(), name="dviewapt"),
]
