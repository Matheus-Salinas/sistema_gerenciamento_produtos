# 📦 Sistema de Gerenciamento de Produtos e Usuários

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.95+-green?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/MySQL-8.0+-blue?logo=mysql" alt="MySQL">
</div>

Este é um projeto desenvolvido com **FastAPI** seguindo a arquitetura **MVC (Model-View-Controller)**. O sistema permite o cadastro, edição, visualização e exclusão de usuários e produtos, com registro de logs de cada operação realizada.

## 🚀 Funcionalidades

- Cadastro de usuários e produtos
- Edição de informações
- Visualização individual e listagem
- Exclusão com confirmação
- Registro de logs para cada operação (CREATE, UPDATE, DELETE)
- Interface HTML renderizada com Jinja2
- Validação de dados nos formulários

## 📁 Estrutura do Projeto

app/
├── controllers/
│   ├── produto_controller.py      
│   └── usuario_controller.py      
│
├── models/
│   ├── database.py                
│   ├── log_model.py               
│   ├── produto_model.py           
│   └── usuario_model.py           
│
├── routes/
│   ├── produto_route.py           
│   └── usuario_route.py 
│         
├── templates/
│   ├── base.html                
│   ├── index.html                 
│   │
│   ├── produtos/
│   │   ├── cadastro.html          
│   │   ├── detalhes.html          
│   │   ├── editar.html            
│   │   └── lista.html             
│   │
│   ├── usuarios/
│   │   ├── cadastro.html          
│   │   ├── detalhes.html          
│   │   ├── editar.html            
│   │   └── lista.html             
│   │
│   └── logs/
│       └── lista.html
│
├── validators/
│   ├── produto_validator.py       
│   └── usuario_validator.py               
│
├── config.py                      
└── main.py    

## 🧑‍💻 Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI**
- **Jinja2**
- **MySQL**
- **Uvicorn**
- **MySQL Connector Python**

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

``` bash
    git clone https://github.com/Matheus-Salinas/sistema_gerenciamento_produtos.git
    cd sistema_gerenciamento_produtos/app
```
### 1. Clone o repositório
``` bash
    python -m venv venv
    source venv/bin/activate  ## Linux/Mac
    venv\Scripts\activate     ## Windows
```

### 3. Instale as dependências
``` bash
    pip install -r requirements.txt
```

Se não tiver o requirements.txt, adicione:

- anyio==4.9.0  
- bcrypt==4.3.0  
- click==8.1.8  
- colorama==0.4.6  
- fastapi==0.95.2  
- h11==0.14.0  
- idna==3.10  
- itsdangerous==2.2.0  
- Jinja2==3.1.6  
- MarkupSafe==3.0.2  
- mysql-connector-python==8.0.33  
- passlib==1.7.4  
- protobuf==3.20.3  
- pydantic==1.10.21  
- python-dotenv==1.0.0  
- python-multipart==0.0.6  
- sniffio==1.3.1  
- starlette==0.27.0  
- typing_extensions==4.13.1  
- uvicorn==0.22.0  


### 4. ⚙️ Configure o Banco de Dados

O arquivo `config.py` é responsável por armazenar as configurações de conexão com o banco de dados MySQL. Ele utiliza variáveis de ambiente para manter a segurança e facilitar a configuração em diferentes ambientes (desenvolvimento, produção, etc).

### 📄 Exemplo do conteúdo do `config.py`

```python
import os

class Config:
    MYSQL_DB = os.getenv('MYSQL_DB', 'nome_do_seu_banco')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'endereco_do_banco')
    MYSQL_USER = os.getenv('MYSQL_USER', 'usuario_do_banco')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'senha_do_banco')
    MYSQL_PORT = os.getenv('MYSQL_PORT', 'porta_do_banco')
```

### 📦 Variáveis de Ambiente Utilizadas

| Variável           | Padrão (default)           | Descrição                               |
|--------------------|----------------------------|------------------------------------------|
| `MYSQL_DB`         | `nome_do_seu_banco`   | Nome do banco de dados                  |
| `MYSQL_HOST`       | `endereco_do_banco`                | Host onde o banco de dados está rodando |
| `MYSQL_USER`       | `usuario_do_banco`                     | Usuário de acesso ao banco              |
| `MYSQL_PASSWORD`   | `senha_do_banco`                  | Senha do banco de dados                 |
| `MYSQL_PORT`       | `porta_do_banco`                     | Porta utilizada para a conexão          |

### ✅ Como definir variáveis de ambiente

Você pode criar um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
MYSQL_DB=nome_do_seu_banco
MYSQL_HOST=endereco_do_banco
MYSQL_USER=usuario_do_banco
MYSQL_PASSWORD=senha_do_banco
MYSQL_PORT=porta_do_banco
```

> 💡 **Dica:** Utilize a biblioteca [`python-dotenv`](https://pypi.org/project/python-dotenv/) para carregar as variáveis automaticamente no seu projeto.

```python
from dotenv import load_dotenv
load_dotenv()  # Coloque isso no início do seu arquivo principal
```

#### Com isso, seu projeto estará configurado para acessar o banco de forma segura e flexível! 🚀


### 5. Execute a aplicação
``` bash
    uvicorn main:app --reload
```

Acesse em: http://127.0.0.1:8000

### ✅ To Do

- Autenticação de usuários

- Paginação nas listagens

- Validações mais robustas com Pydantic

- Exportação de dados

- Upload de imagens


## 🛡️ Dificuldades e Soluções

| Desafio                        | Solução Implementada                                 |
|-------------------------------|--------------------------------------------------------|
| Validação cruzada front/back  | Usamos Pydantic tanto para API quanto templates       |
| Logs detalhados               | Sistema captura estado antes/depois das alterações    |
| Mensagens flash               | Implementação customizada via `request.state`         |
| Segurança de senhas           | Hash `bcrypt` com salt automático                     |

## 📌 Referências

- Documentação FastAPI  
- Passlib (bcrypt)  
- MySQL Connector Python  
- Pydantic Validation  

## Autores

Desenvolvido por Davi Machado e Matheus Salinas, estudantes de Desenvolvimento de Software Multiplataforma na FATEC Itaquera.

## LinkedIn:
- Davi Machado: https://www.linkedin.com/in/davibmachado/
- Matheus Salinas: https://www.linkedin.com/in/matheus-salinas/

