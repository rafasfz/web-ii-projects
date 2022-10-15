from rest_framework.routers import SimpleRouter

from .views import ClienteViewSet, ProdutoViewSet, PedidoViewSet, ClientePedidosViewSet, EstoqueViewSet

router = SimpleRouter()
router.register('clientes', ClienteViewSet, basename='clientes')
router.register('produtos', ProdutoViewSet, basename='produtos')
router.register('pedidos', PedidoViewSet, basename='pedidos')
router.register('clientes_pedidos', ClientePedidosViewSet, basename='clientes-pedidos')
router.register('estoque', EstoqueViewSet, basename='estoque')

urlpatterns = router.urls
