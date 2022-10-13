from rest_framework.viewsets import ModelViewSet

from .models import Cliente, Produto, ItemPedido, Pedido
from .serializers import ClienteSerializer, ProdutoSerializer, ItemPedidoSerializer, PedidoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

