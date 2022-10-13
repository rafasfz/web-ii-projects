from rest_framework import serializers

from .models import Cliente, Produto, ItemPedido, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=255, required=True)
    cpf = serializers.CharField(max_length=11, required=True)

    class Meta:
        model = Cliente
        fields = '__all__'
        ref_name = None

class ProdutoSerializer(serializers.ModelSerializer):
    descricao = serializers.CharField(max_length=255, required=True)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)

    class Meta:
        model = Produto
        fields = '__all__'
        ref_name = None


class PedidoWithoutItemsSerializer(serializers.ModelSerializer):
    data_pedido = serializers.DateTimeField(required=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    status = serializers.CharField(max_length=10, required=True)

    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente', write_only=True)
    
    class Meta:
        model = Pedido
        fields = '__all__'
        ref_name = None

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), source='produto', write_only=True)
    quantidade = serializers.IntegerField(required=True)
    pedido = PedidoWithoutItemsSerializer(read_only=True)
    pedido_id = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all(), source='pedido', write_only=True)

    class Meta:
        model = ItemPedido
        fields = '__all__'


class PedidoSerializer(PedidoWithoutItemsSerializer):
    itens = ItemPedidoSerializer(read_only=True, many=True)
    
    class Meta:
        model = Pedido
        fields = '__all__'

