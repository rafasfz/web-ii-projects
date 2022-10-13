from rest_framework.routers import SimpleRouter

from .views import ClienteViewSet, ProdutoViewSet, ItemPedidoViewSet, PedidoViewSet

router = SimpleRouter()
router.register('clientes', ClienteViewSet, basename='clientes')
router.register('produtos', ProdutoViewSet, basename='produtos')
router.register('itens', ItemPedidoViewSet, basename='itens')
router.register('pedidos', PedidoViewSet, basename='pedidos')

urlpatterns = router.urls
