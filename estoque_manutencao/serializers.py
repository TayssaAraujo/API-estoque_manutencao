from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MaterialManutencao, MovimentacaoEstoque

# 1. SERIALIZER DE MATERIAIS
class MaterialManutencaoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.ReadOnlyField(source='usuario_responsavel.username')

    class Meta:
        model = MaterialManutencao
        fields = ['id', 'nome', 'descricao', 'preco', 'status', 'quantidade_atual', 'usuario_nome']


# 2. SERIALIZER DE MOVIMENTAÇÕES (Atualizado!)
class MovimentacaoEstoqueSerializer(serializers.ModelSerializer):
    # Adiciona o nome do usuário que fez a movimentação para ficar bonito no Bruno
    usuario_nome = serializers.ReadOnlyField(source='usuario_responsavel.username')
    material_nome = serializers.ReadOnlyField(source='material.nome')

    class Meta:
        model = MovimentacaoEstoque
        # TROCADO: Saiu 'condicoes_pagamento' e entrou 'aplicacao' e os campos de leitura
        fields = ['id', 'material', 'material_nome', 'tipo', 'quantidade', 'aplicacao', 'data_movimentacao', 'usuario_nome']


# 3. SERIALIZER DE REGISTRO DE USUÁRIOS
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user


# 4. SERIALIZER PARA LISTAR USUÁRIOS
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']