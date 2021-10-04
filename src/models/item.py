from pydantic import BaseModel


class Item(BaseModel):
    item_id: str
    title: str
    category: str
    subcategory: str
    price: str
    city: str
    url: str
