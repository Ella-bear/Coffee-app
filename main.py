from fastapi import FastAPI, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from . import models, schemas, database
from passlib.context import CryptContext # type: ignore
from typing import List

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# User Registration
@app.post("/register", response_model=schemas.UserCreate)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password, phone_number=user.phone_number, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# User Login
@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

# Update User Profile
@app.put("/update-profile/{user_id}", response_model=schemas.UserUpdate)
def update_profile(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = user_update.name
    user.phone_number = user_update.phone_number
    db.commit()
    db.refresh(user)
    return user

# Get Products
@app.get("/products", response_model=List[schemas.ProductBase])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

# Add to Cart
@app.post("/add-to-cart/{user_id}/{product_id}")
def add_to_cart(user_id: int, product_id: int, cart_item: schemas.CartItemBase, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    total_price = product.price * cart_item.quantity
    cart_item = models.CartItem(user_id=user_id, product_id=product_id, quantity=cart_item.quantity, total_price=total_price)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return {"message": "Item added to cart"}

# Get Cart Items
@app.get("/cart/{user_id}", response_model=List[schemas.CartItemBase])
def get_cart(user_id: int, db: Session = Depends(get_db)):
    cart_items = db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()
    return cart_items

# Remove from Cart
@app.delete("/remove-from-cart/{cart_item_id}")
def remove_from_cart(cart_item_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(models.CartItem).filter(models.CartItem.id == cart_item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(cart_item)
    db.commit()
    return {"message": "Item removed from cart"}

# Payment
@app.post("/payment/{user_id}")
def process_payment(user_id: int, payment_method: str, db: Session = Depends(get_db)):
    if payment_method not in ["card", "paypal"]:
        raise HTTPException(status_code=400, detail="Invalid payment method")
    return {"message": f"Payment processed via {payment_method}"}