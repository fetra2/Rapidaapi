from django.urls import path
from . import views
from .views import RegisterUser, ProtectedView
#from .views import LoginUser
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

#api imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tarification API",
        default_version='v1',
        description="You will find all available tarifs.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rasolonjatovofetra@gmail.com"),
        license=openapi.License(name="Ftr license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#path("tarif/api/v1/<int:zone>/<str:poids>/", views.tarif, name="tarif"),

urlpatterns = [
	path("",  views.index),
    path("tarif/form", views.formTarif, name="formtarif"),

    path('register', RegisterUser.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protected', ProtectedView.as_view(), name='protected'),

    path('api/bureaux', views.Bureau.as_view(), name='bureau'),
    path('api/zone/<int:codique1>/<int:codique2>', views.ZoneByCodique.as_view(), name='zone'),

    path('api/tarifs', views.TarifList.as_view(), name='tarif-list'),
    #path('api/tarifs/<int:pk>/', views.TarifDetail.as_view(), name='tarif-detail'),
    path('api/tarifs/<int:zone>/<str:poids>', views.TarifZonePoids.as_view(), name='tarif-zone-poids'),
    path('api/tarifs/zone/<int:zone>', views.TarifZone.as_view(), name='tarif-zone'),

    path('swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]