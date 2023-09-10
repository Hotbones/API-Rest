from django.urls import path,include
from rest_framework import routers
from app_api import views

router=routers.DefaultRouter()
router.register(r'Molo',views.MoloViewSet)

urlpatterns = [
    path('', include(router.urls))
]