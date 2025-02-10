from pydantic import BaseModel # type: ignore

class UserCreate(BaseModel):
    email: str
    password: str
    phone_number: str
    name: str

class UserUpdate(BaseModel):
    name: str
    phone_number: str

class ProductBase(BaseModel):
    name: str
    price: float
    category: str
    image_url: str

class ProductCreate(ProductBase):
    pass

class CartItemBase(BaseModel):
    product_id: int
    quantity: int