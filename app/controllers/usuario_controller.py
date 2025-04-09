import logging
import mysql.connector
from typing import Optional
from fastapi import Depends, HTTPException, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.database import get_db
from models.log_model import registrar_log
from models.usuario_model import (
    UsuarioCreate, 
    get_all_usuarios, 
    get_usuario_by_id, 
    create_usuario, 
    delete_usuario, 
    update_usuario
)


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


async def listar_usuarios(request: Request, db: mysql.connector.MySQLConnection = Depends(get_db)):
    """
    Lista todos os usuários cadastrados no sistema.
    
    Args:
        request: Objeto Request do FastAPI
        db: Conexão com o banco de dados
    
    Returns:
        TemplateResponse: Renderiza a página de listagem de usuários
    """
    try:
        usuarios = get_all_usuarios(db)
        flash = get_flash(request)
        messages = [flash] if flash else []
        return templates.TemplateResponse(
            "usuarios/lista.html",
            {"request": request, "usuarios": usuarios, "messages": messages}
        )
    except Exception as e:
        logger.error(f"Erro ao listar usuários: {str(e)}", exc_info=True)
        return templates.TemplateResponse(
            "usuarios/lista.html",
            {"request": request, "usuarios": [], "messages": [{"message": "Erro ao carregar usuários", "category": "danger"}]}
        )

async def form_cadastrar_usuario(request: Request):
    """
    Exibe o formulário de cadastro de novo usuário.
    
    Args:
        request: Objeto Request do FastAPI
    
    Returns:
        TemplateResponse: Renderiza o formulário de cadastro
    """
    return templates.TemplateResponse(
        "usuarios/cadastro.html",
        {"request": request, "errors": [], "form_data": {}}
    )

async def cadastrar_usuario(
    request: Request,
    nome: str = Form(..., min_length=3, max_length=50),
    email: str = Form(..., regex=r"^[a-z0-9_.]+@[a-z0-9-]+\.[a-z0-9-.]+$"),
    senha: str = Form(..., min_length=6),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Processa o formulário de cadastro de novo usuário.
    
    Args:
        request: Objeto Request do FastAPI
        nome: Nome completo do usuário
        email: E-mail do usuário
        senha: Senha do usuário
        db: Conexão com o banco de dados
    
    Returns:
        RedirectResponse: Redireciona para a lista de usuários após cadastro bem-sucedido
        TemplateResponse: Retorna ao formulário com erros se houver problemas
    """
    try:
        usuario_data = UsuarioCreate(nome=nome, email=email, senha=senha)
        usuario_id = create_usuario(usuario_data, db)
        
        if not usuario_id:
            raise ValueError("Não foi possível criar o usuário")
        
        
        registrar_log(
            tipo_operacao="CREATE",
            tabela_afetada="usuarios",
            id_registro=usuario_id,
            dados_novos=usuario_data.dict(),
            request=request,
            db=db
        )
        
        set_flash(request, "Usuário cadastrado com sucesso!")
        return RedirectResponse(
            url="/usuarios",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except mysql.connector.Error as e:
        if e.errno == 1062:  
            error_msg = "Este e-mail já está cadastrado"
        else:
            error_msg = f"Erro no banco de dados: {str(e)}"
        logger.error(error_msg)
        return templates.TemplateResponse(
            "usuarios/cadastro.html",
            {
                "request": request,
                "errors": [error_msg],
                "form_data": {"nome": nome, "email": email}
            }
        )
    except Exception as e:
        logger.error(f"Erro ao cadastrar usuário: {str(e)}", exc_info=True)
        return templates.TemplateResponse(
            "usuarios/cadastro.html",
            {
                "request": request,
                "errors": [str(e)],
                "form_data": {"nome": nome, "email": email}
            }
        )

async def obter_usuario(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Exibe os detalhes de um usuário específico.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do usuário
        db: Conexão com o banco de dados
    
    Returns:
        TemplateResponse: Renderiza a página de detalhes do usuário
    """
    try:
        usuario = get_usuario_by_id(id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        return templates.TemplateResponse(
            "usuarios/detalhes.html",
            {"request": request, "usuario": usuario}
        )
    except Exception as e:
        logger.error(f"Erro ao obter usuário {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao carregar usuário"
        )

async def form_editar_usuario(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Exibe o formulário de edição de usuário.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do usuário a ser editado
        db: Conexão com o banco de dados
    
    Returns:
        TemplateResponse: Renderiza o formulário de edição
    """
    try:
        usuario = get_usuario_by_id(id, db)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        return templates.TemplateResponse(
            "usuarios/editar.html",
            {"request": request, "usuario": usuario, "errors": []}
        )
    except Exception as e:
        logger.error(f"Erro ao carregar formulário de edição para usuário {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao carregar formulário de edição"
        )

async def processar_edicao_usuario(
    request: Request,
    id: int,
    nome: str = Form(..., min_length=3, max_length=50),
    email: str = Form(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"),
    senha: Optional[str] = Form(None, min_length=6),
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Processa o formulário de edição de usuário.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do usuário a ser editado
        nome: Novo nome do usuário
        email: Novo e-mail do usuário
        senha: Nova senha (opcional)
        db: Conexão com o banco de dados
    
    Returns:
        RedirectResponse: Redireciona para os detalhes do usuário após edição bem-sucedida
        TemplateResponse: Retorna ao formulário com erros se houver problemas
    """
    try:
        usuario_atual = get_usuario_by_id(id, db)
        
        update_data = {"nome": nome, "email": email}
        if senha and senha.strip():
            update_data["senha"] = senha
        
        rows_updated = update_usuario(id, update_data, db)
        if rows_updated == 0:
            raise ValueError("Nenhum usuário foi atualizado")
        
        
        registrar_log(
            tipo_operacao="UPDATE",
            tabela_afetada="usuarios",
            id_registro=id,
            dados_anteriores={
                "nome": usuario_atual["nome"],
                "email": usuario_atual["email"]
            },
            dados_novos=update_data,
            request=request,
            db=db
        )
        
        set_flash(request, "Usuário atualizado com sucesso!")
        return RedirectResponse(
            url=f"/usuarios/{id}",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except mysql.connector.Error as e:
        if e.errno == 1062:  
            error_msg = "Este e-mail já está cadastrado"
        else:
            error_msg = f"Erro no banco de dados: {str(e)}"
        logger.error(error_msg)
        usuario = get_usuario_by_id(id, db)
        return templates.TemplateResponse(
            "usuarios/editar.html",
            {
                "request": request,
                "usuario": usuario,
                "errors": [error_msg]
            }
        )
    except Exception as e:
        logger.error(f"Erro ao editar usuário {id}: {str(e)}", exc_info=True)
        usuario = get_usuario_by_id(id, db)
        return templates.TemplateResponse(
            "usuarios/editar.html",
            {
                "request": request,
                "usuario": usuario,
                "errors": [str(e)]
            }
        )

async def deletar_usuario(
    request: Request,
    id: int,
    db: mysql.connector.MySQLConnection = Depends(get_db)
):
    """
    Remove um usuário do sistema.
    
    Args:
        request: Objeto Request do FastAPI
        id: ID do usuário a ser removido
        db: Conexão com o banco de dados
    
    Returns:
        RedirectResponse: Redireciona para a lista de usuários após remoção bem-sucedida
    """
    try:
        usuario = get_usuario_by_id(id, db)
        
        affected_rows = delete_usuario(id, db)
        if affected_rows == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        
        registrar_log(
            tipo_operacao="DELETE",
            tabela_afetada="usuarios",
            id_registro=id,
            dados_anteriores={
                "nome": usuario["nome"],
                "email": usuario["email"]
            },
            request=request,
            db=db
        )
        
        set_flash(request, "Usuário excluído com sucesso!")
        return RedirectResponse(
            url="/usuarios",
            status_code=status.HTTP_303_SEE_OTHER
        )
    except Exception as e:
        logger.error(f"Erro ao deletar usuário {id}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Erro ao deletar usuário"
        )