from fastapi import APIRouter, Depends, HTTPException, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr
from models.usuario_model import (
    UsuarioCreate, 
    get_all_usuarios, 
    get_usuario_by_id, 
    create_usuario, 
    delete_usuario, 
    update_usuario
)
from models.database import get_db
import mysql.connector
from typing import Optional

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, name="listar_usuarios")
async def listar_usuarios(request: Request, db: mysql.connector.MySQLConnection = Depends(get_db)):
    try:
        usuarios = get_all_usuarios(db)
        return templates.TemplateResponse(
            "usuarios/lista.html",
            {"request": request, "usuarios": usuarios, "messages": []}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "usuarios/lista.html",
            {"request": request, "usuarios": [], "messages": [("danger", f"Erro ao carregar usuários: {str(e)}")]}
        )

@router.get("/cadastrar", response_class=HTMLResponse, name="form_cadastrar_usuario")
async def form_cadastrar_usuario(request: Request):
    return templates.TemplateResponse(
        "usuarios/cadastro.html",
        {"request": request, "errors": [], "form_data": {}}
    )

@router.post("/cadastrar", response_class=HTMLResponse, name="cadastrar_usuario")
async def cadastrar_usuario(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        if len(senha) < 6:
            raise ValueError("A senha deve ter no mínimo 6 caracteres")
        
        usuario_data = UsuarioCreate(nome=nome, email=email, senha=senha)
        usuario_id = create_usuario(usuario_data, db)
        
        if not usuario_id:
            raise ValueError("Não foi possível criar o usuário")
            
        return RedirectResponse(
            url=router.url_path_for("listar_usuarios"),
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        return templates.TemplateResponse(
            "usuarios/cadastro.html",
            {
                "request": request,
                "errors": [str(e)],
                "form_data": {"nome": nome, "email": email}
            }
        )

@router.get("/{id}", response_class=HTMLResponse, name="obter_usuario")
async def obter_usuario(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        usuario = get_usuario_by_id(id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        return templates.TemplateResponse(
            "usuarios/detalhes.html",
            {"request": request, "usuario": usuario}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao carregar usuário: {str(e)}"
        )

@router.get("/{id}/editar", response_class=HTMLResponse, name="form_editar_usuario")
async def form_editar_usuario(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        usuario = get_usuario_by_id(id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        return templates.TemplateResponse(
            "usuarios/editar.html",
            {"request": request, "usuario": usuario, "errors": []}
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao carregar formulário de edição: {str(e)}"
        )

@router.post("/{id}/editar", response_class=HTMLResponse, name="processar_edicao_usuario")
async def processar_edicao_usuario(
    request: Request,
    id: int,
    nome: str = Form(...),
    email: str = Form(...),
    senha: Optional[str] = Form(None),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        update_data = {"nome": nome, "email": email}
        if senha and senha.strip():
            if len(senha) < 6:
                raise ValueError("A senha deve ter no mínimo 6 caracteres")
            update_data["senha"] = senha
        
        rows_updated = update_usuario(id, update_data, db)
        if rows_updated == 0:
            raise ValueError("Nenhum usuário foi atualizado")
            
        return RedirectResponse(
            url=router.url_path_for("obter_usuario", id=id),
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        usuario = get_usuario_by_id(id, db)
        return templates.TemplateResponse(
            "usuarios/editar.html",
            {
                "request": request,
                "usuario": usuario,
                "errors": [str(e)]
            }
        )

@router.post("/{id}/deletar", name="deletar_usuario")
async def deletar_usuario(
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    try:
        affected_rows = delete_usuario(id, db)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        return RedirectResponse(
            url=router.url_path_for("listar_usuarios"),
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao deletar usuário: {str(e)}"
        )