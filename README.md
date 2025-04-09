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

## Relatorio de Uso 

## **Usuarios**

### ▶ Listar Usuarios (GET)
`ENDPOINT:` `/produtos`

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2>Lista de Usuários</h2>
        <a href="http://127.0.0.1:8000/usuarios/cadastrar" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Cadastrar Usuário
        </a>
    </div>

    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th class="table-actions">Ações</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td>6</td>
                    <td>Davi Bernardes</td>
                    <td>daviteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/6" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/6/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/6/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td>David</td>
                    <td>davidteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/10" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/10/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/10/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td>Matheus Salinas Zancope</td>
                    <td>matheusteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/5" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/5/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/5/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>11</td>
                    <td>Wellingthon</td>
                    <td>weweteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/11" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/11/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/11/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
### ▶ Cadastrar Usuarios (POST)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2>Lista de Usuários</h2>
        <a href="http://127.0.0.1:8000/usuarios/cadastrar" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Cadastrar Usuário
        </a>
    </div>

    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th class="table-actions">Ações</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td>12</td>
                    <td>Carlos Lionel</td>
                    <td>carlosteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/12" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/12/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/12/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>6</td>
                    <td>Davi Bernardes</td>
                    <td>daviteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/6" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/6/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/6/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td>David</td>
                    <td>davidteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/10" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/10/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/10/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td>Matheus Salinas Zancope</td>
                    <td>matheusteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/5" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/5/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/5/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>11</td>
                    <td>Wellingthon</td>
                    <td>weweteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/11" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/11/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/11/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
### ▶ Obter Usuario (GET)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container mt-4">
    <h2 class="mb-4">Detalhes do Usuário</h2>
    
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h5 class="card-title">Carlos Lionel</h5>
                    <div class="card-text">
                        <p><strong>ID:</strong> 12</p>
                        <p><strong>Email:</strong> carlosteste@gmail.com</p>
                    </div>
                </div>
            </div>
            
            <div class="d-flex gap-2 mt-4">
                <a href="http://127.0.0.1:8000/usuarios/12/editar" class="btn btn-warning">
                    <i class="bi bi-pencil"></i> Editar
                </a>
                
                <form method="POST" action="http://127.0.0.1:8000/usuarios/12/deletar" class="d-inline">
                    <button type="submit" class="btn btn-danger" 
                            onclick="return confirm('Tem certeza que deseja excluir este usuário?')">
                        <i class="bi bi-trash"></i> Excluir
                    </button>
                </form>
                
                <a href="http://127.0.0.1:8000/usuarios/" class="btn btn-secondary ms-auto">
                    <i class="bi bi-arrow-left"></i> Voltar para Lista
                </a>
            </div>
        </div>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
### ▶ Editar Usuario (POST)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container mt-4">
    <h2 class="mb-4">Detalhes do Usuário</h2>
    
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h5 class="card-title">carlos</h5>
                    <div class="card-text">
                        <p><strong>ID:</strong> 12</p>
                        <p><strong>Email:</strong> caloreditado@gmail.com</p>
                    </div>
                </div>
            </div>
            
            <div class="d-flex gap-2 mt-4">
                <a href="http://127.0.0.1:8000/usuarios/12/editar" class="btn btn-warning">
                    <i class="bi bi-pencil"></i> Editar
                </a>
                
                <form method="POST" action="http://127.0.0.1:8000/usuarios/12/deletar" class="d-inline">
                    <button type="submit" class="btn btn-danger" 
                            onclick="return confirm('Tem certeza que deseja excluir este usuário?')">
                        <i class="bi bi-trash"></i> Excluir
                    </button>
                </form>
                
                <a href="http://127.0.0.1:8000/usuarios/" class="btn btn-secondary ms-auto">
                    <i class="bi bi-arrow-left"></i> Voltar para Lista
                </a>
            </div>
        </div>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```

### ▶ Deletar Usuario (POST)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2>Lista de Usuários</h2>
        <a href="http://127.0.0.1:8000/usuarios/cadastrar" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Cadastrar Usuário
        </a>
    </div>

    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th class="table-actions">Ações</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td>6</td>
                    <td>Davi Bernardes</td>
                    <td>daviteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/6" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/6/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/6/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td>David</td>
                    <td>davidteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/10" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/10/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/10/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td>Matheus Salinas Zancope</td>
                    <td>matheusteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/5" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/5/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/5/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>11</td>
                    <td>Wellingthon</td>
                    <td>weweteste@gmail.com</td>
                    <td>
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/usuarios/11" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/usuarios/11/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form action="http://127.0.0.1:8000/usuarios/11/deletar" 
                                  method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
## **Produto**

### ▶ Listar Produto (GET)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2>Lista de Produtos</h2>
        <a href="http://127.0.0.1:8000/produtos/cadastrar" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Cadastrar Produto
        </a>
    </div>

    

    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Preço</th>
                    <th>Estoque</th>
                    <th class="text-end">Ações</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td>4</td>
                    <td>Tênis Nike</td>
                    <td>R$ 300.00</td>
                    <td>2</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/4" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/4/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/4/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td>Jaqueta</td>
                    <td>R$ 250.00</td>
                    <td>3</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/5" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/5/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/5/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>7</td>
                    <td>Oculos Marrom</td>
                    <td>R$ 180.00</td>
                    <td>5</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/7" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/7/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/7/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>8</td>
                    <td>Jaqueta G</td>
                    <td>R$ 234.00</td>
                    <td>12</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/8" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/8/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/8/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td>Amendoim</td>
                    <td>R$ 123.00</td>
                    <td>1</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/10" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/10/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/10/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>13</td>
                    <td>Lápis</td>
                    <td>R$ 10.00</td>
                    <td>30</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/13" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/13/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/13/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>14</td>
                    <td>Cama de cachorro</td>
                    <td>R$ 12.00</td>
                    <td>3</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/14" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/14/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/14/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
### ▶ Cadastrar Produto (POST)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2>Lista de Produtos</h2>
        <a href="http://127.0.0.1:8000/produtos/cadastrar" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Cadastrar Produto
        </a>
    </div>

    

    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Preço</th>
                    <th>Estoque</th>
                    <th class="text-end">Ações</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td>4</td>
                    <td>Tênis Nike</td>
                    <td>R$ 300.00</td>
                    <td>2</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/4" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/4/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/4/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td>Jaqueta</td>
                    <td>R$ 250.00</td>
                    <td>3</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/5" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/5/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/5/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>7</td>
                    <td>Oculos Marrom</td>
                    <td>R$ 180.00</td>
                    <td>5</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/7" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/7/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/7/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>8</td>
                    <td>Jaqueta G</td>
                    <td>R$ 234.00</td>
                    <td>12</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/8" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/8/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/8/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td>Amendoim</td>
                    <td>R$ 123.00</td>
                    <td>1</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/10" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/10/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/10/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>13</td>
                    <td>Lápis</td>
                    <td>R$ 10.00</td>
                    <td>30</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/13" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/13/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/13/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>14</td>
                    <td>Cama de cachorro</td>
                    <td>R$ 12.00</td>
                    <td>3</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/14" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/14/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/14/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>15</td>
                    <td>Camiseta Caveira</td>
                    <td>R$ 80.00</td>
                    <td>4</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/15" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/15/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/15/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
### ▶ Obter Produto (GET)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container mt-4">
    <h2 class="mb-4">Detalhes do Produto</h2>
    
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Camiseta Caveira</h5>
            <div class="card-text">
                <p><strong>ID:</strong> 15</p>
                <p><strong>Descrição:</strong> camiseta preta</p>
                <p><strong>Preço:</strong> R$ 80.00</p>
                <p><strong>Estoque:</strong> 4 unidades</p>
            </div>
            
            <div class="d-flex gap-2 mt-4">
                <a href="http://127.0.0.1:8000/produtos/15/editar" class="btn btn-warning">
                    <i class="bi bi-pencil"></i> Editar
                </a>
                
                <form method="POST" action="http://127.0.0.1:8000/produtos/15/deletar" class="d-inline">
                    <button type="submit" class="btn btn-danger" 
                            onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                        <i class="bi bi-trash"></i> Excluir
                    </button>
                </form>
                
                <a href="http://127.0.0.1:8000/produtos/" class="btn btn-secondary ms-auto">
                    <i class="bi bi-arrow-left"></i> Voltar para Lista
                </a>
            </div>
        </div>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```
### ▶ Editar Produto (POST)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container mt-4">
    <h2 class="mb-4">Detalhes do Produto</h2>
    
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Camiseta de gatinho</h5>
            <div class="card-text">
                <p><strong>ID:</strong> 15</p>
                <p><strong>Descrição:</strong> Nenhuma descrição</p>
                <p><strong>Preço:</strong> R$ 19.00</p>
                <p><strong>Estoque:</strong> 2 unidades</p>
            </div>
            
            <div class="d-flex gap-2 mt-4">
                <a href="http://127.0.0.1:8000/produtos/15/editar" class="btn btn-warning">
                    <i class="bi bi-pencil"></i> Editar
                </a>
                
                <form method="POST" action="http://127.0.0.1:8000/produtos/15/deletar" class="d-inline">
                    <button type="submit" class="btn btn-danger" 
                            onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                        <i class="bi bi-trash"></i> Excluir
                    </button>
                </form>
                
                <a href="http://127.0.0.1:8000/produtos/" class="btn btn-secondary ms-auto">
                    <i class="bi bi-arrow-left"></i> Voltar para Lista
                </a>
            </div>
        </div>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```

### ▶ Deletar Produto (POST)

**Exemplo de resposta:**
``` bash
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gerenciamento</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .invalid-feedback { display: block; }
        .table-actions { white-space: nowrap; width: 1%; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">
                <i class="bi bi-box-seam"></i> Sistema de Gerenciamento
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/produtos/">
                        <i class="bi bi-box-seam"></i> Produtos
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/usuarios/">
                        <i class="bi bi-people"></i> Usuários
                    </a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        

        
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2>Lista de Produtos</h2>
        <a href="http://127.0.0.1:8000/produtos/cadastrar" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> Cadastrar Produto
        </a>
    </div>

    

    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Preço</th>
                    <th>Estoque</th>
                    <th class="text-end">Ações</th>
                </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td>4</td>
                    <td>Tênis Nike</td>
                    <td>R$ 300.00</td>
                    <td>2</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/4" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/4/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/4/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>5</td>
                    <td>Jaqueta</td>
                    <td>R$ 250.00</td>
                    <td>3</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/5" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/5/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/5/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>7</td>
                    <td>Oculos Marrom</td>
                    <td>R$ 180.00</td>
                    <td>5</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/7" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/7/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/7/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>8</td>
                    <td>Jaqueta G</td>
                    <td>R$ 234.00</td>
                    <td>12</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/8" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/8/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/8/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>10</td>
                    <td>Amendoim</td>
                    <td>R$ 123.00</td>
                    <td>1</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/10" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/10/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/10/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>13</td>
                    <td>Lápis</td>
                    <td>R$ 10.00</td>
                    <td>30</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/13" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/13/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/13/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
                <tr>
                    <td>14</td>
                    <td>Cama de cachorro</td>
                    <td>R$ 12.00</td>
                    <td>3</td>
                    <td class="text-end">
                        <div class="btn-group btn-group-sm">
                            <a href="http://127.0.0.1:8000/produtos/14" 
                               class="btn btn-info" title="Visualizar">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="http://127.0.0.1:8000/produtos/14/editar" 
                               class="btn btn-warning" title="Editar">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <form method="POST" action="http://127.0.0.1:8000/produtos/14/deletar" 
                                  class="d-inline">
                                <button type="submit" class="btn btn-danger" 
                                        title="Excluir"
                                        onclick="return confirm('Tem certeza que deseja excluir este produto?')">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </form>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
</div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Ativar validação de formulários
        (function() {
            'use strict'
            const forms = document.querySelectorAll('.needs-validation')
            
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
        })()
    </script>
</body>
</html>
```

## Autores

Desenvolvido por Davi Machado e Matheus Salinas, estudantes de Desenvolvimento de Software Multiplataforma na FATEC Itaquera.

## LinkedIn:
- Davi Machado: https://www.linkedin.com/in/davibmachado/
- Matheus Salinas: https://www.linkedin.com/in/matheus-salinas/

