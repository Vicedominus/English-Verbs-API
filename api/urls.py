from django.urls import path

from .views import  VerbSearchListAPIView,  VerbRetrieveAPIView



urlpatterns = [
    path('verbs/', VerbSearchListAPIView.as_view(), name='search'),
    path('verbs/<int:pk>', VerbRetrieveAPIView.as_view(), name='retrieve'),
]

