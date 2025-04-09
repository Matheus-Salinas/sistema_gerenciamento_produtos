from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.produto_route import router as produto_router
from routes.usuario_route import router as usuario_router


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(produto_router)
app.include_router(usuario_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Rota principal que exibe a página inicial.
    
    Args:
        request: Objeto Request do FastAPI
    
    Returns:
        TemplateResponse: Renderiza a página inicial
    """
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)