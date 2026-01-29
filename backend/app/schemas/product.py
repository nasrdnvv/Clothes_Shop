from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100,
                      description='Product Name')
    description: Optional[str] = Field(None, description='Product Description')
    price: float = Field(..., gt=0,
                         description='Product price(Must Be Greater Than 0')
    category_id: int = Field(..., description='Category ID')
    image_url: Optional[str] = Field(None, description='Product Image URL')

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description='Unique Product ID')
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description='Product Category Details')

    class Config:
        form_attributes = True

class ProductListResponse(ProductBase):
    products: list[ProductResponse]
    total: int = Field(..., description='Total Product Count')



