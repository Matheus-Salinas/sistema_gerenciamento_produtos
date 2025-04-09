import logging
import mysql.connector
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Form, Request, status
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
from routes.usuarios_routes import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

