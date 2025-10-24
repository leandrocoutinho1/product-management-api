from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import User, Product
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_data():
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    if db.query(User).count() == 0:
        hashed_pw = pwd_context.hash("admin123")
        admin = User(username="admin", hashed_password=hashed_pw)
        db.add(admin)
        db.commit()
        print("✅ Usuário admin criado!")

    if db.query(Product).count() == 0:
        products = [
            Product(name="Notebook Lenovo", price=4500.00, category="Eletrônicos"),
            Product(name="Cadeira Gamer", price=1200.00, category="Móveis"),
            Product(name='Monitor LG 24"', price=900.00, category="Eletrônicos"),
        ]
        db.add_all(products)
        db.commit()
        print("✅ Banco populado com produtos iniciais!")

    db.close()


if __name__ == "__main__":
    seed_data()
