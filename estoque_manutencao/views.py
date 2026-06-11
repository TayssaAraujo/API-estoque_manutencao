from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# 1. IMPORTAÇÃO DOS MODELOS
from .models import MaterialManutencao, MovimentacaoEstoque

# 2. IMPORTAÇÃO DOS SERIALIZERS (Exatamente como estão no seu arquivo)
from .serializers import (
    MaterialManutencaoSerializer,
    MovimentacaoEstoqueSerializer,
    UserRegisterSerializer,
    UserListSerializer
)


# 3. VIEWSET DE MATERIAIS
class MaterialManutencaoViewSet(viewsets.ModelViewSet):
    queryset = MaterialManutencao.objects.all()
    serializer_class = MaterialManutencaoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario_responsavel=self.request.user)

    @action(detail=False, methods=['get'], url_path='criticos')
    def criticos(self, request):
        materiais_criticos = MaterialManutencao.objects.filter(quantidade_atual__lt=5)
        serializer = self.get_serializer(materiais_criticos, many=True)
        return Response({
            "total_itens_criticos": materiais_criticos.count(),
            "status_relatorio": "Atenção: Necessita de Reposição urgente",
            "itens": serializer.data
        })


# 2. VIEWSET DE MOVIMENTAÇÕES
class MovimentacaoEstoqueViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoEstoque.objects.all()
    serializer_class = MovimentacaoEstoqueSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 1. Pega os dados da movimentação que está sendo criada
        movimentacao = serializer.save(usuario_responsavel=self.request.user)

        # 2. Pega o material que está sofrendo a movimentação
        material = movimentacao.material

        # 3. Lógica matemática: Verifica se é Entrada ou Saída
        if movimentacao.tipo == 'ENTRADA':
            material.quantidade_atual += movimentacao.quantidade
        elif movimentacao.tipo == 'SAIDA':
            material.quantidade_atual -= movimentacao.quantidade

            # Validação opcional de segurança para o estoque não ficar negativo
            if material.quantidade_atual < 0:
                material.quantidade_atual = 0

                # 4. Salva a nova quantidade calculada no banco de dados
        material.save()


# 5. VIEW DE REGISTRO
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


# 6. VIEW DE LISTAGEM DE USUÁRIOS
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]