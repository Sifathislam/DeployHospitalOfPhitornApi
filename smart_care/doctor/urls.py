from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

router.register('list', views.DoctorViewSet)
router.register('spacialization', views.SpacializationViewSet)
router.register('designation', views.DasignationViewSet)
router.register('avaiabletime', views.AvailableTimeViewSet)
router.register('review', views.DoctorViewSet)

urlpatterns = [
    path('', include(router.urls))
]