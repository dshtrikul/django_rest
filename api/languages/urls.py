from django.urls import path, include
from .views import LanguageView, FamilyView, CountryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('family', FamilyView)
router.register('country', CountryView)

urlpatterns = [
    path('', include(router.urls))
]
