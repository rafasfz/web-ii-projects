from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

class Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    cpf = models.CharField(max_length=11, verbose_name="CPF")


class Pedido(models.Model):
    class StatusChoices(models.TextChoices):
        REALIZADO = 'Realizado'
        CANCELADO = 'Cancelado'

    data_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente") 
    # itens 
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.REALIZADO, verbose_name="Status")


class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
