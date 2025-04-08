from pydantic import BaseModel, Field, validator
from typing import Optional
import mysql.connector
from datetime import datetime

class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=3, example="Notebook")
    descricao: Optional[str] = Field(None, example="Notebook i7 16GB RAM")
    preco: float = Field(..., gt=0, example=4500.90)
    estoque: int = Field(..., ge=0, example=10)

    @validator('nome')
    def nome_deve_ter_minimo_3_caracteres(cls, v):
        if len(v.strip()) < 3:
            raise ValueError('O nome deve ter pelo menos 3 caracteres')
        return v.title()

    @validator('preco')
    def preco_deve_ser_positivo(cls, v):
        if v <= 0:
            raise ValueError('O preço deve ser positivo')
        return round(v, 2)

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

def get_produto_by_id(id: int, db: mysql.connector.MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, nome, descricao, preco, estoque, 
               criado_em, atualizado_em 
        FROM produtos WHERE id = %s
    """, (id,))
    return cursor.fetchone()

def get_all_produtos(db: mysql.connector.MySQLConnection):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, nome, descricao, preco, estoque, 
               criado_em, atualizado_em 
        FROM produtos ORDER BY criado_em DESC
    """)
    return cursor.fetchall()

def create_produto(produto: ProdutoCreate, db: mysql.connector.MySQLConnection):
    cursor = db.cursor()
    cursor.execute(
        """INSERT INTO produtos 
        (nome, descricao, preco, estoque) 
        VALUES (%s, %s, %s, %s)""",
        (produto.nome, produto.descricao, produto.preco, produto.estoque),
    )
    db.commit()
    return cursor.lastrowid

def update_produto(id: int, produto: ProdutoBase, db: mysql.connector.MySQLConnection):
    cursor = db.cursor()
    cursor.execute(
        """UPDATE produtos 
        SET nome=%s, descricao=%s, preco=%s, estoque=%s, 
            atualizado_em=CURRENT_TIMESTAMP 
        WHERE id=%s""",
        (produto.nome, produto.descricao, produto.preco, produto.estoque, id),
    )
    db.commit()
    return cursor.rowcount

def delete_produto(id: int, db: mysql.connector.MySQLConnection):
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    db.commit()
    return cursor.rowcount