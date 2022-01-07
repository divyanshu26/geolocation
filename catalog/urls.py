from django.urls import include, path
from rest_framework import routers

from .views import ListPersons

from . import views


router = routers.DefaultRouter()
#router.register(r'people', ListPersons, basename='Person')

urlpatterns = [
    path('', include(router.urls)),
    path('people/', views.ListPersons.as_view(),name='people')
]
