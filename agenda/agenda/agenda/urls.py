from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contactos.views import (
    contactosViewSet,
    categoriasViewSet,
    enderecosViewSet,
    notaViewSet
)

router = DefaultRouter()
router.register(r'contactos', contactosViewSet, basename='contactos')
router.register(r'categorias', categoriasViewSet, basename='categorias')
router.register(r'enderecos', enderecosViewSet, basename='enderecos')
router.register(r'nota', notaViewSet, basename='nota')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]