from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.product_model import Product
from app.dtos.product_dto import ProductDTO
from app.auth.jwt_bearer import JWTBearer

router = APIRouter(prefix="/api/produtos", tags=["Produtos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", dependencies=[Depends(JWTBearer())])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/{id}", dependencies=[Depends(JWTBearer())])
def get_product(id: int, db: Session = Depends(get_db)):
    produto = db.query(Product).filter(Product.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.post("/", dependencies=[Depends(JWTBearer())])
def create_product(produto: ProductDTO, db: Session = Depends(get_db)):
    novo = Product(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.put("/{id}", dependencies=[Depends(JWTBearer())])
def update_product(id: int, produto: ProductDTO, db: Session = Depends(get_db)):
    db_produto = db.query(Product).filter(Product.id == id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    for key, value in produto.dict().items():
        setattr(db_produto, key, value)
    
    db.commit()
    db.refresh(db_produto)
    return db_produto


@router.delete("/{id}", dependencies=[Depends(JWTBearer())])
def delete_product(id: int, db: Session = Depends(get_db)):
    db_produto = db.query(Product).filter(Product.id == id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(db_produto)
    db.commit()
    return {"message": "Produto removido com sucesso"}
