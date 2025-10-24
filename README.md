# Product Management API

API para gerenciar produtos com autenticação JWT, usando **FastAPI**, **SQLAlchemy** e **PostgreSQL**.  

---

## 📁 Estrutura do Projeto

```
product-management-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── seed.py
│   ├── config.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── auth_controller.py
│   │   ├── jwt_bearer.py
│   │   └── jwt_handler.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── product_controller.py
│   ├── dtos/
│   │   ├── __init__.py
│   │   ├── product_dto.py
│   │   └── user_dto.py
│   └── models/
│       ├── __init__.py
│       ├── product_model.py
│       └── user_model.py
├── insomnia/
│   └── product-management-api.yaml
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

## 💻 Pré-requisitos

- Python 3.9+
- Docker & Docker Compose
- Git

---

## 🚀 Rodando a aplicação

### 1. Clonar o repositório

```bash
git clone https://github.com/leandrocoutinho1/product-management-api.git
cd product-management-api
```

### 2. Configurar variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

O arquivo `.env` já está configurado com os valores padrão que funcionam com o Docker Compose:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/products_db
JWT_SECRET=meusegredosuperseguro
JWT_ALGORITHM=HS256
```

> **⚠️ Importante:** Em produção, altere o `JWT_SECRET` para uma chave forte e aleatória!

### 3. Criar ambiente virtual (opcional, para rodar scripts Python localmente)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 4. Instalar dependências (opcional, local sem Docker)

```bash
pip install -r requirements.txt
```

### 5. Subir os containers com Docker

```bash
docker-compose up --build
```

Isso irá criar os containers da API e do banco PostgreSQL.

---

## 🗂 Inicializar banco com dados de exemplo

Após os containers estarem rodando, execute o script seed para popular alguns produtos iniciais:

```bash
docker exec -it product_api python -m app.seed
```

O script criará as tabelas e adicionará produtos iniciais, caso não existam.

---

## 📖 Documentação Interativa (Swagger)

Após subir os containers, acesse a documentação interativa da API:

🔗 **http://localhost:8000/docs**

Por lá é fácil e auto explicativo realizar os testes de todas as rotas disponíveis.

---

## 🔑 Rotas da API

### Auth

**POST /auth/register** → Registrar novo usuário

Body JSON:

```json
{
  "username": "usuario1",
  "password": "senha123"
}
```

**POST /auth/login** → Login do usuário

Body JSON:

```json
{
  "username": "usuario1",
  "password": "senha123"
}
```

Resposta:

```json
{
  "access_token": "<TOKEN_JWT>",
  "token_type": "bearer"
}
```

### Produtos (necessário token JWT no Header `Authorization: Bearer <TOKEN>`)

**GET /api/produtos** → Lista todos os produtos

**GET /api/produtos/{id}** → Busca produto por ID

**POST /api/produtos** → Cria novo produto

Body JSON:

```json
{
  "name": "Teclado Mecânico",
  "price": 250.00,
  "category": "Eletrônicos"
}
```

**PUT /api/produtos/{id}** → Atualiza produto

Body JSON:

```json
{
  "name": "Teclado Mecânico RGB",
  "price": 300.00,
  "category": "Eletrônicos"
}
```

**DELETE /api/produtos/{id}** → Remove produto

---

## 📝 Testando a API com Insomnia

### Importar a Collection

O projeto inclui uma collection pronta do Insomnia com todos os endpoints configurados:

📁 **Arquivo:** `insomnia/product-management-api.yaml`

### Como importar:

1. Abra o Insomnia
2. Clique em **Application** → **Preferences** → **Data** → **Import Data**
3. Selecione o arquivo `insomnia/product-management-api.yaml`
4. A collection **Product Management API** será importada com:
   - ✅ Todos os endpoints de Auth e Produtos
   - ✅ Exemplos de requisições prontas
   - ✅ Variáveis de ambiente configuradas

### Configuração do Token JWT:

Após rodar o **Login -> auth/login/**, o Insomnia automaticamente salva o `access_token` na variável de ambiente e ele será utilizado nas requisições autenticadas.

> ✨ **Automático!** Não é necessário copiar e colar o token manualmente.

---

## ⚡ Observações

- Sempre utilize o token JWT retornado no login para acessar rotas protegidas.
- Ao derrubar os containers e remover o volume `product-management-api_postgres_data`, você irá zerar o banco e precisará rodar a seed novamente.
