from fastapi import APIRouter, Depends, HTTPException, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from controllers.produto_controller import (
    listar_produtos,
    form_cadastrar_produto,
    cadastrar_produto,
    obter_produto,
    form_editar_produto,
    processar_edicao_produto,
    deletar_produto
)
from models.database import get_db

router = APIRouter(prefix="/produtos", tags=["produtos"])

router.get("/", response_class=HTMLResponse, name="listar_produtos")(listar_produtos)
router.get("/cadastrar", response_class=HTMLResponse, name="produto_cadastrar")(form_cadastrar_produto)
router.post("/cadastrar", response_class=HTMLResponse, name="produto_cadastrar_post")(cadastrar_produto)
router.get("/{id}", response_class=HTMLResponse, name="produto_detalhes")(obter_produto)
router.get("/{id}/editar", response_class=HTMLResponse, name="produto_editar")(form_editar_produto)
router.post("/{id}/editar", response_class=HTMLResponse, name="produto_editar_post")(processar_edicao_produto)
router.post("/{id}/deletar", name="produto_deletar")(deletar_produto)