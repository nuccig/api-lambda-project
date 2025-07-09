# 🔌 API Lambda Project

## 📋 Descrição
API RESTful desenvolvida com AWS Chalice para gerenciamento de clientes (pessoas físicas e jurídicas) executada em ambiente serverless AWS Lambda.

## 🚀 Tecnologias Utilizadas
- **Python 3.12**
- **AWS Chalice** - Framework para criação de APIs serverless
- **AWS Lambda** - Execução serverless
- **Pytest** - Testes unitários

## 📁 Estrutura do Projeto
```
apis/
└── customers/
    └── customers/
        ├── app.py              # API principal com rotas CRUD
        ├── requirements.txt    # Dependências de produção
        ├── requirements-dev.txt # Dependências de desenvolvimento
        ├── chalicelib/         # Bibliotecas auxiliares
        └── tests/              # Testes unitários
```

## ⚡ Funcionalidades
### Pessoas Físicas (`/customers/person`)
- **POST** - Criar novo usuário
- **PUT** - Atualizar usuário existente
- **DELETE** - Deletar usuário
- **GET** - Buscar usuário por nome

### Pessoas Jurídicas (`/customers/company`)
- **POST** - Criar nova empresa
- **PUT** - Atualizar empresa existente
- **DELETE** - Deletar empresa
- **GET** - Buscar empresa por nome

## 🔧 Instalação e Execução
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar testes
pytest tests/

# Deploy para AWS
chalice deploy
```

## 🛠️ Configuração
O projeto utiliza simulação de banco de dados em memória para demonstração. Em produção, recomenda-se integração com DynamoDB ou RDS.

## 📦 Dependências Principais
- chalice
- boto3 (para integração AWS)

## 🧪 Testes
Os testes estão localizados em `tests/test_app.py` e cobrem todas as rotas da API com diferentes cenários de validação.
