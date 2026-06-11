from django.db import models
from django.contrib.auth.models import User


# ==========================================
# 1. MODEL DE MATERIAL (Fica sempre no topo!)
# ==========================================
class MaterialManutencao(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('INDISPONIVEL', 'Indisponível'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='DISPONIVEL')
    quantidade_atual = models.IntegerField(default=0)
    usuario_responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# ==========================================
# 2. MODEL DE MOVIMENTAÇÃO (Fica embaixo!)
# ==========================================
class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada (Abastecimento)'),
        ('SAIDA', 'Saída (Baixa/Consumo)'),
    ]

    # Usando string 'MaterialManutencao' para evitar qualquer erro de leitura do Django
    material = models.ForeignKey('MaterialManutencao', on_delete=models.CASCADE, related_name='movimentacoes')
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    usuario_responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    # Campo aplicação adicionado no lugar de condições de pagamento
    aplicacao = models.CharField(max_length=255, default="", help_text="Onde o material foi aplicado ou motivo da entrada")

    def __str__(self):
        return f"{self.tipo} - {self.quantidade} un de {self.material.nome}"