from fastapi import APIRouter, Depends, HTTPException, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from controllers.usuario_controller import (
    listar_usuarios,
    form_cadastrar_usuario,
    cadastrar_usuario,
    obter_usuario,
    form_editar_usuario,
    processar_edicao_usuario,
    deletar_usuario
)
from models.database import get_db

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

router.get("/", response_class=HTMLResponse, name="listar_usuarios")(listar_usuarios)
router.get("/cadastrar", response_class=HTMLResponse, name="form_cadastrar_usuario")(form_cadastrar_usuario)
router.post("/cadastrar", response_class=HTMLResponse, name="cadastrar_usuario")(cadastrar_usuario)
router.get("/{id}", response_class=HTMLResponse, name="obter_usuario")(obter_usuario)
router.get("/{id}/editar", response_class=HTMLResponse, name="form_editar_usuario")(form_editar_usuario)
router.post("/{id}/editar", response_class=HTMLResponse, name="processar_edicao_usuario")(processar_edicao_usuario)
router.post("/{id}/deletar", name="deletar_usuario")(deletar_usuario)