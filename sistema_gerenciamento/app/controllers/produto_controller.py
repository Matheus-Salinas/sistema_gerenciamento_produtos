from fastapi import APIRouter, Depends, HTTPException, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from models.produto_model import ProdutoCreate, get_all_produtos, get_produto_by_id, create_produto, update_produto, delete_produto
from models.database import get_db
import mysql.connector

router = APIRouter()
templates = Jinja2Templates(directory="templates")


class ProdutoSchema(BaseModel):
    nome: str
    descricao: Optional[str] = ""
    preco: float
    estoque: int


@router.get("/", response_class=HTMLResponse)
def listar_produtos(request: Request, db: mysql.connector.MySQLConnection = Depends(get_db)):
    produtos = get_all_produtos(db)
    return templates.TemplateResponse("produtos/lista.html", {"request": request, "produtos": produtos})


@router.get("/cadastrar", response_class=HTMLResponse)
def form_cadastrar_produto(request: Request):
    return templates.TemplateResponse("produtos/cadastro.html", {"request": request})


@router.post("/cadastrar")
def cadastrar_produto(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    estoque: int = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db),
):
    produto_data = ProdutoCreate(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
    produto_id = create_produto(produto_data, db)

    if produto_id:
        return RedirectResponse(url="/produtos", status_code=303)

    return templates.TemplateResponse("produtos/cadastro.html", {
        "request": request,
        "errors": ["Erro ao cadastrar produto"]
    })


@router.get("/{id}", response_class=HTMLResponse)
def obter_produto(request: Request, id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    produto = get_produto_by_id(id, db)
    if produto:
        return templates.TemplateResponse("produtos/detalhes.html", {"request": request, "produto": produto})
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.get("/{id}/editar", response_class=HTMLResponse)
def form_editar_produto(request: Request, id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    produto = get_produto_by_id(id, db)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return templates.TemplateResponse("produtos/editar.html", {"request": request, "produto": produto})


@router.post("/{id}/editar")
def editar_produto(
    request: Request,
    id: int,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    estoque: int = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db),
):
    produto_data = ProdutoCreate(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
    affected_rows = update_produto(id, produto_data, db)

    if affected_rows > 0:
        return RedirectResponse(url="/produtos", status_code=303)

    raise HTTPException(status_code=400, detail="Nenhum produto foi atualizado")


@router.post("/{id}/deletar")
def deletar_produto(id: int, db: mysql.connector.MySQLConnection = Depends(get_db)):
    affected_rows = delete_produto(id, db)
    if affected_rows > 0:
        return RedirectResponse(url="/produtos", status_code=303)
    raise HTTPException(status_code=404, detail="Produto não encontrado")
