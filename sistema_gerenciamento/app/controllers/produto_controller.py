from fastapi import APIRouter, Depends, HTTPException, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from models.produto_model import (
    ProdutoCreate, 
    ProdutoUpdate,
    ProdutoResponse,
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
from typing import List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/produtos", tags=["produtos"])
templates = Jinja2Templates(directory="templates")

# ==================== HELPERS ====================
def set_flash(request: Request, message: str, category: str = "success"):
    if not hasattr(request.state, 'session'):
        request.state.session = {}
    request.state.session['flash'] = {'message': message, 'category': category}

def get_flash(request: Request):
    if hasattr(request.state, 'session') and 'flash' in request.state.session:
        flash = request.state.session.pop('flash')
        return flash
    return None

# ==================== API REST ====================
@router.get("/api", response_model=List[ProdutoResponse])
async def listar_produtos_api(db: mysql.connector.MySQLConnection = Depends(get_db)):
    try:
        return get_all_produtos(db)
    except Exception as e:
        logger.error(f"Erro ao listar produtos: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao listar produtos"
        )

@router.get("/api/{id}", response_model=ProdutoResponse)
async def obter_produto_api(
    id: int, 
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    produto = get_produto_by_id(id, db)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    return produto

@router.post("/api", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
async def criar_produto_api(
    produto: ProdutoCreate, 
    request: Request,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        produto_id = create_produto(produto, db)
        if not produto_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Não foi possível criar o produto"
            )
        
        registrar_log(
            tipo_operacao="CREATE",
            tabela_afetada="produtos",
            id_registro=produto_id,
            dados_novos=produto.dict(),
            request=request,
            db=db
        )
        
        novo_produto = get_produto_by_id(produto_id, db)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=novo_produto
        )
    except Exception as e:
        logger.error(f"Erro ao criar produto: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/api/{id}", response_model=ProdutoResponse)
async def atualizar_produto_api(
    id: int,
    produto: ProdutoUpdate,
    request: Request,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        produto_atual = get_produto_by_id(id, db)
        if not produto_atual:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )
        
        rows_updated = update_produto(id, produto, db)
        if rows_updated == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nenhum produto foi atualizado"
            )
        
        registrar_log(
            tipo_operacao="UPDATE",
            tabela_afetada="produtos",
            id_registro=id,
            dados_anteriores={
                "nome": produto_atual["nome"],
                "descricao": produto_atual["descricao"],
                "preco": produto_atual["preco"],
                "estoque": produto_atual["estoque"]
            },
            dados_novos=produto.dict(),
            request=request,
            db=db
        )
        
        produto_atualizado = get_produto_by_id(id, db)
        return produto_atualizado
    except Exception as e:
        logger.error(f"Erro ao atualizar produto {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/api/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_produto_api(
    id: int,
    request: Request,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    produto = get_produto_by_id(id, db)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    affected_rows = delete_produto(id, db)
    if affected_rows == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum produto foi removido"
        )
    
    registrar_log(
        tipo_operacao="DELETE",
        tabela_afetada="produtos",
        id_registro=id,
        dados_anteriores={
            "nome": produto["nome"],
            "descricao": produto["descricao"],
            "preco": produto["preco"],
            "estoque": produto["estoque"]
        },
        request=request,
        db=db
    )
    
    return None

# ==================== INTERFACE WEB ====================
@router.get("/", response_class=HTMLResponse, name="listar_produtos")
async def listar_produtos_html(
    request: Request,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        produtos = get_all_produtos(db)
        flash = get_flash(request)
        messages = [flash] if flash else []
        return templates.TemplateResponse(
            "produtos/lista.html",
            {
                "request": request,
                "produtos": produtos,
                "messages": messages,
                "active_page": "produtos"
            }
        )
    except Exception as e:
        logger.error(f"Erro ao listar produtos: {str(e)}", exc_info=True)
        return templates.TemplateResponse(
            "produtos/lista.html",
            {
                "request": request,
                "produtos": [],
                "messages": [{"message": "Erro ao carregar produtos", "category": "danger"}],
                "active_page": "produtos"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/cadastrar", response_class=HTMLResponse, name="produto_cadastrar")
async def form_cadastrar_produto(request: Request):
    return templates.TemplateResponse(
        "produtos/cadastro.html",
        {
            "request": request,
            "errors": [],
            "form_data": {},
            "active_page": "produtos"
        }
    )

@router.post("/cadastrar", response_class=HTMLResponse, name="produto_cadastrar_post")
async def cadastrar_produto(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    estoque: int = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    errors = []
    form_data = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "estoque": estoque
    }
    
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
                "form_data": form_data,
                "active_page": "produtos"
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )

    try:
        produto_data = ProdutoCreate(**form_data)
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
            url=router.url_path_for("listar_produtos"),
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {str(e)}", exc_info=True)
        errors.append("Ocorreu um erro ao cadastrar o produto")
        return templates.TemplateResponse(
            "produtos/cadastro.html",
            {
                "request": request,
                "errors": errors,
                "form_data": form_data,
                "active_page": "produtos"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/{id}", response_class=HTMLResponse, name="produto_detalhes")
async def obter_produto_html(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        produto = get_produto_by_id(id, db)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        return templates.TemplateResponse(
            "produtos/detalhes.html",
            {
                "request": request,
                "produto": produto,
                "active_page": "produtos"
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao obter produto {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao carregar produto"
        )

@router.get("/{id}/editar", response_class=HTMLResponse, name="produto_editar")
async def form_editar_produto(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        produto = get_produto_by_id(id, db)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        return templates.TemplateResponse(
            "produtos/editar.html",
            {
                "request": request,
                "produto": produto,
                "errors": [],
                "active_page": "produtos"
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao carregar formulário de edição para produto {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao carregar formulário de edição"
        )

@router.post("/{id}/editar", response_class=HTMLResponse, name="produto_editar_post")
async def processar_edicao_produto(
    request: Request,
    id: int,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    estoque: int = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    errors = []
    form_data = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "estoque": estoque
    }
    
    if len(nome.strip()) < 3:
        errors.append("O nome do produto deve ter no mínimo 3 caracteres")
    if preco <= 0:
        errors.append("O preço deve ser um valor positivo")
    if estoque < 0:
        errors.append("O estoque deve ser um número inteiro maior ou igual a zero")
    
    if errors:
        return templates.TemplateResponse(
            "produtos/editar.html",
            {
                "request": request,
                "produto": {"id": id, **form_data},
                "errors": errors,
                "active_page": "produtos"
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )

    try:
        produto_atual = get_produto_by_id(id, db)
        if not produto_atual:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
        produto_data = ProdutoUpdate(**form_data)
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
            url=router.url_path_for("produto_detalhes", id=id),
            status_code=status.HTTP_303_SEE_OTHER
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao editar produto {id}: {str(e)}", exc_info=True)
        errors.append("Ocorreu um erro ao atualizar o produto")
        return templates.TemplateResponse(
            "produtos/editar.html",
            {
                "request": request,
                "produto": {"id": id, **form_data},
                "errors": errors,
                "active_page": "produtos"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.post("/{id}/deletar", name="produto_deletar")
async def deletar_produto_html(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        produto = get_produto_by_id(id, db)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        
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
            url=router.url_path_for("listar_produtos"),
            status_code=status.HTTP_303_SEE_OTHER
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao deletar produto {id}: {str(e)}", exc_info=True)
        set_flash(request, "Erro ao excluir produto", "danger")
        return RedirectResponse(
            url=router.url_path_for("listar_produtos"),
            status_code=status.HTTP_303_SEE_OTHER
        )