from pydantic import BaseModel, Field
from typing import List, Optional

class InvoiceItem(BaseModel):
    """提取的单个商品明细项"""
    item_name: str = Field(description="The name or description of the item purchased")
    quantity: int = Field(description="The quantity of the item")
    unit_price: float = Field(description="The price per unit of the item")

class ExtractionResult(BaseModel):
    """发票/订单的整体提取结果"""
    company_name: str = Field(description="The name of the vendor or company issuing the document")
    invoice_date: Optional[str] = Field(description="Date of the invoice in YYYY-MM-DD format", default=None)
    total_amount: float = Field(description="The total monetary amount of the invoice")
    currency: str = Field(description="The currency of the transaction, e.g., USD, EUR, CNY", default="USD")
    items: List[InvoiceItem] = Field(description="List of items found in the document", default_factory=list)

class ExtractionRequest(BaseModel):
    """API 接收的请求载荷"""
    raw_text: str = Field(..., description="The highly unstructured text from OCR, Email, or PDF")