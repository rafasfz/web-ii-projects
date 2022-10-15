from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Cliente, Produto, Pedido, Estoque
from .serializers import ClienteSerializer, ProdutoSerializer, PedidoSerializer, ClientePedidosSerializer, EstoqueSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ClientePedidosViewSet(ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientePedidosSerializer

class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
