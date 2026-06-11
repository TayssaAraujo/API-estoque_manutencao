from django.contrib import admin
from estoque_manutencao.models import MaterialManutencao, MovimentacaoEstoque

@admin.register(MaterialManutencao)
class MaterialManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade_atual', 'status', 'usuario_responsavel')
    list_filter = ('status', 'usuario_responsavel')
    search_fields = ('nome', 'descricao')

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'tipo', 'quantidade', 'data_movimentacao')
    list_filter = ('tipo', 'data_movimentacao')
    search_fields = ('material__nome', 'condicoes_pagamento')
