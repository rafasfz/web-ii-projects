from rest_framework import serializers

from .models import Cliente, Produto, ItemPedido, Pedido, Estoque

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

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), source='produto', write_only=True)
    quantidade = serializers.IntegerField(required=True)

    class Meta:
        model = ItemPedido
        fields = ('produto', 'produto_id', 'quantidade')


class PedidoSerializer(serializers.ModelSerializer):
    data_pedido = serializers.DateTimeField(required=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    status = serializers.ChoiceField(choices=Pedido.StatusChoices.choices, default=Pedido.StatusChoices.REALIZADO)

    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente', write_only=True)
    itens = ItemPedidoSerializer(many=True)

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        total = 0
        for item in itens_data:
            produto = Produto.objects.get(pk=item['produto'].id)
            estoque = Estoque.objects.get(produto=produto)
            if estoque.quantidade < item['quantidade']:
                raise serializers.ValidationError(f'Quantidade em estoque de {produto.descricao} insuficiente')
            total += produto.preco * item['quantidade']
            Estoque.objects.filter(pk=estoque.id).update(quantidade=estoque.quantidade - item['quantidade'])
        pedido = Pedido.objects.create(**validated_data, total=total)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido

    def update(self, pedido, validated_data):
        for item in pedido.itens.all():
            estoque = Estoque.objects.get(produto=item.produto)
            estoque.quantidade += item.quantidade
            estoque.save()
            item.delete() 
        itens_data = validated_data.pop('itens')
        total = 0
        for item in itens_data:
            produto = Produto.objects.get(pk=item['produto'].id)
            estoque = Estoque.objects.get(produto=produto)
            if estoque.quantidade < item['quantidade']:
                raise serializers.ValidationError(f'Quantidade em estoque de {produto.descricao} insuficiente')
            total += produto.preco * item['quantidade']
            Estoque.objects.filter(pk=estoque.id).update(quantidade=estoque.quantidade - item['quantidade'])
        Pedido.objects.filter(pk=pedido.id).update(**validated_data, total=total)
        pedido = Pedido.objects.get(
            pk=pedido.id,
        )
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido

    
    class Meta:
        model = Pedido
        fields = '__all__'


class ClientePedidosSerializer(ClienteSerializer):
    pedidos = PedidoSerializer(many=True)

    class Meta:
        model = Cliente
        fields = '__all__'
        ref_name = None


class EstoqueSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), source='produto', write_only=True)
    quantidade = serializers.IntegerField(required=True)

    class Meta:
        model = Estoque
        fields = '__all__'
        ref_name = None

