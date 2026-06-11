from estoque_manutencao.views import MaterialManutencaoViewSet, MovimentacaoEstoqueViewSet, UserRegisterView
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from estoque_manutencao.views import MaterialManutencaoViewSet, MovimentacaoEstoqueViewSet

# Importações obrigatórias para o Swagger (drf_yasg) funcionar
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração da página de documentação do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Estoque de Manutenção",
        default_version='v1',
        description="Trabalho A3 - Sistemas Distribuídos e Mobile",
        contact=openapi.Contact(email="seu-email@faseh.edu.br"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'materiais', MaterialManutencaoViewSet)
router.register(r'movimentacoes', MovimentacaoEstoqueViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # EXIGÊNCIA DO ROTEIRO: Área Pública (Autenticação JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # NOVA ROTA PÚBLICA PARA CRIAÇÃO DE USUÁRIOS
    path('api/usuarios/registrar/', UserRegisterView.as_view(), name='registrar_usuario'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rotas da Documentação da API (Área Pública)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
