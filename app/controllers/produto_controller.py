from fastapi import Depends, HTTPException, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.produto_model import (
    ProdutoCreate,
    get_all_produtos,
    get_produto_by_id,
    create_produto,
    update_produto,
    delete_produto
)
from models.database import get_db
from models.log_model import registrar_log
import mysql.connector
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


templates = Jinja2Templates(directory="templates")


def set_flash(request: Request, message: str, category: str = "success"):
    """Define uma mensagem flash na sessão."""
    if not hasattr(request.state, 'session'):
        request.state.session = {}
    request.state.session['flash'] = {'message': message, 'category': category}

def get_flash(request: Request):
    """Obtém e remove a mensagem flash da sessão."""
    if hasattr(request.state, 'session') and 'flash' in request.state.session:
        flash = request.state.session.pop('flash')
        return flash
    return None


async def listar_produtos(request: Request, db: mysql.connector.MySQLConnection = Depends(get_db)):
    """
    Lista todos os produtos disponíveis.
    
    Args:
        request: Objeto Request do FastAPI
        db: Conexão com o banco de dados
    
    Returns:
        TemplateResponse: Renderiza a página de listagem de produtos
    """
    try:
        produtos = get_all_produtos(db)
        flash = get_flash(request)
        messages = [flash] if flash else []
        return templates.TemplateResponse(
            "produtos/lista.html",
            {"request": request, "produtos": produtos, "messages": messages}
        )
    except Exception as e:
        logger.error(f"Erro ao listar produtos: {str(e)}", exc_info=True)
        return templates.TemplateResponse(
            "produtos/lista.html",
            {"request": request, "produtos": [], "messages": [{"message": "Erro ao carregar produtos", "category": "danger"}]}
        )

async def form_cadastrar_produto(request: Request):
    """
    Exibe o formulário de cadastro de novo produto.
    
    Args:
        request: Objeto Request do FastAPI
    
    Returns:
        TemplateResponse: Renderiza o formulário de cadastro
    """
    return templates.TemplateResponse(
        "produtos/cadastro.html",
        {"request": request, "errors": [], "form_data": {}}
    )

async def cadastrar_produto(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    estoque: int = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Processa o formulário de cadastro de novo produto.
    
    Args:
        request: Objeto Request do FastAPI
        nome: Nome do produto
        descricao: Descrição do produto
        preco: Preço do produto
        estoque: Quantidade em estoque
        db: Conexão com o banco de dados
    
    Returns:
        RedirectResponse: Redireciona para a lista de produtos após cadastro bem-sucedido
        TemplateResponse: Retorna ao formulário com erros se houver problemas
    """
    errors = []
    
    if len(nome.strip()) < 3:
        errors.append("O nome do produto deve ter no mínimo 3 caracteres")
    if preco <= 0:
        errors.append("O preço deve ser um valor positivo")
    if estoque < 0:
        errors.append("O estoque deve ser um número inteiro maior ou igual a zero")
    
    if errors:
        return templates.TemplateResponse(
            "produtos/cadastro.html",
            {
                "request": request,
                "errors": errors,
                "form_data": {
                    "nome": nome,
                    "descricao": descricao,
                    "preco": preco,
                    "estoque": estoque
                }
            }
        )

    try:
        produto_data = ProdutoCreate(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
        produto_id = create_produto(produto_data, db)

        if not produto_id:
            raise ValueError("Não foi possível criar o produto")
        
        
        registrar_log(
            tipo_operacao="CREATE",
            tabela_afetada="produtos",
            id_registro=produto_id,
            dados_novos=produto_data.dict(),
            request=request,
            db=db
        )
        
        set_flash(request, "Produto cadastrado com sucesso!")
        return RedirectResponse(
            url="/produtos",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {str(e)}", exc_info=True)
        errors.append(f"Erro ao cadastrar produto: {str(e)}")
        return templates.TemplateResponse(
            "produtos/cadastro.html",
            {
                "request": request,
                "errors": errors,
                "form_data": {
                    "nome": nome,
                    "descricao": descricao,
                    "preco": preco,
                    "estoque": estoque
                }
            }
        )

async def obter_produto(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Exibe os detalhes de um produto específico.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do produto
        db: Conexão com o banco de dados
    
    Returns:
        TemplateResponse: Renderiza a página de detalhes do produto
    """
    try:
        produto = get_produto_by_id(id, db)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        return templates.TemplateResponse(
            "produtos/detalhes.html",
            {"request": request, "produto": produto}
        )
    except Exception as e:
        logger.error(f"Erro ao obter produto {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao carregar produto"
        )

async def form_editar_produto(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Exibe o formulário de edição de produto.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do produto a ser editado
        db: Conexão com o banco de dados
    
    Returns:
        TemplateResponse: Renderiza o formulário de edição
    """
    try:
        produto = get_produto_by_id(id, db)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        return templates.TemplateResponse(
            "produtos/editar.html",
            {"request": request, "produto": produto, "errors": []}
        )
    except Exception as e:
        logger.error(f"Erro ao carregar formulário de edição para produto {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao carregar formulário de edição"
        )

async def processar_edicao_produto(
    request: Request,
    id: int,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    estoque: int = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Processa o formulário de edição de produto.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do produto a ser editado
        nome: Novo nome do produto
        descricao: Nova descrição do produto
        preco: Novo preço do produto
        estoque: Nova quantidade em estoque
        db: Conexão com o banco de dados
    
    Returns:
        RedirectResponse: Redireciona para os detalhes do produto após edição bem-sucedida
        TemplateResponse: Retorna ao formulário com erros se houver problemas
    """
    try:
        errors = []
        
        # Validações
        if len(nome.strip()) < 3:
            errors.append("O nome do produto deve ter no mínimo 3 caracteres")
        if preco <= 0:
            errors.append("O preço deve ser um valor positivo")
        if estoque < 0:
            errors.append("O estoque deve ser um número inteiro maior ou igual a zero")
        
        if errors:
            produto = {
                "id": id,
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "estoque": estoque
            }
            return templates.TemplateResponse(
                "produtos/editar.html",
                {
                    "request": request,
                    "produto": produto,
                    "errors": errors
                }
            )

        produto_atual = get_produto_by_id(id, db)
        produto_data = ProdutoCreate(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
        rows_updated = update_produto(id, produto_data, db)

        if rows_updated == 0:
            raise ValueError("Nenhum produto foi atualizado")
        
       
        registrar_log(
            tipo_operacao="UPDATE",
            tabela_afetada="produtos",
            id_registro=id,
            dados_anteriores={
                "nome": produto_atual["nome"],
                "descricao": produto_atual["descricao"],
                "preco": float(produto_atual["preco"]),
                "estoque": produto_atual["estoque"]
            },
            dados_novos=produto_data.dict(),
            request=request,
            db=db
        )
        
        set_flash(request, "Produto atualizado com sucesso!")
        return RedirectResponse(
            url=f"/produtos/{id}",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        logger.error(f"Erro ao editar produto {id}: {str(e)}", exc_info=True)
        produto = get_produto_by_id(id, db)
        return templates.TemplateResponse(
            "produtos/editar.html",
            {
                "request": request,
                "produto": produto,
                "errors": [str(e)]
            }
        )

async def deletar_produto(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Remove um produto do sistema.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do produto a ser removido
        db: Conexão com o banco de dados
    
    Returns:
        RedirectResponse: Redireciona para a lista de produtos após remoção bem-sucedida
    """
    try:
        produto = get_produto_by_id(id, db)
        
        affected_rows = delete_produto(id, db)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        
        registrar_log(
            tipo_operacao="DELETE",
            tabela_afetada="produtos",
            id_registro=id,
            dados_anteriores={
                "nome": produto["nome"],
                "descricao": produto["descricao"],
                "preco": float(produto["preco"]),
                "estoque": produto["estoque"]
            },
            request=request,
            db=db
        )
        
        set_flash(request, "Produto excluído com sucesso!")
        return RedirectResponse(
            url="/produtos",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        logger.error(f"Erro ao deletar produto {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao deletar produto"
        )