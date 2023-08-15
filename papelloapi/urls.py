from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from pedidos.views import PedidosViewSet, ClienteViewSet, ListaPedidosDoCliente, ClientePorId_clienteViewSet, ClientePorLocalizacaoViewSet, PedidoPorNumeroPedidoViewSet, ProdutoViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Papello API",
      default_version='v1',
      description="API feita par manipular dados referentes aos pedidos",
      terms_of_service="",
      contact=openapi.Contact(email="automacao@papello.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('pedidos', PedidosViewSet , basename='Pedidos')
router.register('clientes', ClienteViewSet , basename='Clientes')
router.register('produtos', ProdutoViewSet , basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('clientes/<int:id_cliente>/pedidos', ListaPedidosDoCliente.as_view()),
    path('clientes/<int:id_cliente>', ClientePorId_clienteViewSet.as_view()),
    path('clientes/<str:UF>', ClientePorLocalizacaoViewSet.as_view()),
    path('pedidos/<str:numero_pedido>', PedidoPorNumeroPedidoViewSet.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
