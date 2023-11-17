from django.urls import path
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CORPS RAPIDA API",
        default_version='v1',
        description="You will find all available tarifs.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rasolonjatovofetra@gmail.com"),
        license=openapi.License(name="Ftr license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
	path("",  views.index),

    path('api/clients', views.PersonneList.as_view(), name='personne-list'),
    path('api/clients/<str:pk>', views.PersonneDetail.as_view(), name='personne-detail'),
    path('api/envois', views.EnvoiList.as_view(), name='envoi-list'),
    path('api/envois/<str:pk>', views.EnvoiDetail.as_view(), name='envoi-detail'),
    path('api/factures', views.FactureList.as_view(), name='facture-list'),
    path('api/factures/<str:pk>', views.FactureDetail.as_view(), name='facture-detail'),
    path('api/histo', views.HistoriqueList.as_view(), name='historique-list'),
    path('api/histo/<str:pk>', views.HistoriqueDetail.as_view(), name='historique-detail'),
    path('api/axes', views.AxeList.as_view(), name='axe-list'),
    path('api/axes/<str:pk>', views.AxeDetail.as_view(), name='axe-detail'),
    path('api/documents', views.DocList.as_view(), name='doc-list'),
    path('api/documents/<str:pk>', views.DocDetail.as_view(), name='doc-detail'),

    path('swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]