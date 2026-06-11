# Sistema de Controle de Estoque para Manutenção Industrial STOCK  (API RESTful)

Este repositório contém a API RESTful desenvolvida em Django e Django REST Framework (DRF) para o controle de entradas, saídas e gestão de estoque crítico de materiais de manutenção industrial. O sistema conta com autenticação segura via JWT (JSON Web Tokens), controle de usuários e atualização automática de saldo de estoque.

---

## Tecnologias Utilizadas

* **Python 3.13**
* **Django 5.1.6**
* **Django REST Framework (DRF)**
* **Simple JWT** (Autenticação via Token)
* **SQLite** (Banco de dados de desenvolvimento)
* **Drf-Yasg / Swagger** (Documentação automatizada da API)

---

## ⚙Configuração do Ambiente Local

Siga os passos abaixo para clonar, instalar as dependências e rodar o projeto em sua máquina:

### 1. Clonar o Repositório e Entrar na Pasta

```bash
git clone <url-do-seu-repositorio>

```

```bash
cd API-RestFul

```

### 2. Ativar o Ambiente Virtual (`.venv`)

* **Windows (PowerShell):**

```bash
.\.venv\Scripts\Activate.ps1

```

* **Windows (Git Bash/Prompt):**

```bash
source .venv/Scripts/activate

```

### 3. Instalar as Dependências Básicas (Caso mude de ambiente)

```bash
pip install django djangorestframework djangorestframework-simplejwt drf-yasg

```

### 4. Atualizar o Banco de Dados (Migrações)

```bash
python manage.py makemigrations

```

```bash
python manage.py migrate

```

### 5. Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver

```

O servidor estará rodando localmente no endereço: `http://127.0.0.1:8000/`

---

##  URLs de Acesso Direto e Rotas da Plataforma

Com o servidor rodando (`runserver`), você pode acessar as seguintes interfaces diretamente pelo seu navegador de internet:

###  Interfaces Visuais (Navegador)

| Rota / Interface | URL de Acesso Direto | Descrição |
| --- | --- | --- |
| **Painel Administrativo** | [http://127.0.0.1:8000/admin/](https://www.google.com/search?q=http://127.0.0.1:8000/admin/) | Interface nativa do Django para gerenciar usuários, cadastros, materiais e visualizar o histórico de movimentações. |
| **Documentação Swagger** | [http://127.0.0.1:8000/swagger/](https://www.google.com/search?q=http://127.0.0.1:8000/swagger/) | Tela interativa contendo todas as rotas da API, formatos de JSON aceitos, parâmetros e testes de requisições em tempo real. |
| **Documentação Redoc** | [http://127.0.0.1:8000/redoc/](https://www.google.com/search?q=http://127.0.0.1:8000/redoc/) | Uma documentação estática, limpa e organizada para leitura dos endpoints da API. |

---

### Endpoints da API (Testes via Bruno / Postman / Insomnia)

> **Nota de Segurança:** Todas as rotas de Materiais e Movimentações exigem o cabeçalho de autenticação: `Authorization: Bearer <seu_access_token>`. O token gerado no Login tem duração de *1* horas**.

####  Autenticação e Usuários

* **Criar Novo Usuário:** `POST /api/usuarios/registrar/` *(Acesso Livre)*
* *Campos:* `username`, `password`, `email`


* **Listar Usuários Cadastrados:** `GET /api/usuarios/` *(Requer Token)*
* **Gerar Token (Login):** `POST /api/token/` *(Acesso Livre)*
* *Retorno:* `access` (Token de Acesso - 2 horas) e `refresh` (7 dias)


* **Renovar Token (Refresh):** `POST /api/token/refresh/`
* *Envia:* O código contido em `"refresh"` para receber um novo `"access"` sem deslogar.



####  Gestão de Materiais (`/api/materiais/`)

* **Listar Todos os Materiais:** `GET /api/materiais/`
* **Cadastrar Material:** `POST /api/materiais/`
* *Campos:* `nome`, `descricao`, `preco`, `status`, `quantidade_atual`


* **Visualizar um Material Específico:** `GET /api/materiais/<id>/`
* **Editar Informações do Material:** `PUT` ou `PATCH /api/materiais/<id>/`
* **Deletar Peça do Estoque:** `DELETE /api/materiais/<id>/`
* **Relatório de Estoque Crítico:** `GET /api/materiais/criticos/`
* *Regra de Negócio:* Retorna de forma inteligente todos os itens cuja `quantidade_atual` é **menor que 5 unidades**, emitindo um alerta de reposição urgente.



####  Movimentações de Estoque (`/api/movimentacoes/`)

* **Histórico Geral de Movimentações:** `GET /api/movimentacoes/`
* **Registrar Entrada ou Saída (Baixa):** `POST /api/movimentacoes/`
* *Campos obrigatórios:* `material` (ID), `tipo` (`"ENTRADA"` ou `"SAIDA"`), `quantidade`, `aplicacao`
* *Lógica de Negócio Automatizada:*
* Ao enviar `"tipo": "ENTRADA"`, o sistema soma automaticamente a quantidade enviada ao saldo atual do material.
* Ao enviar `"tipo": "SAIDA"`, o sistema subtrai automaticamente a quantidade do saldo atual (com trava de segurança para não negativar estoque).
* O campo `aplicacao` armazena a justificativa industrial (ex: *"Manutenção corretiva na Ponte Rolante"*).





---

## 👥 Desenvolvedores (Grupo Acadêmico)

Trabalho desenvolvido como entrega da avaliação **A3** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

* Tayssa Rodrigues de Araújo
* Marcos Bitencourt

```

```