"""Product data model."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Product:
    """Product data model."""

    name: str
    price: float
    unit: str
    category: str
    source: str
    scraped_at: datetime
    url: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'name': self.name,
            'price': self.price,
            'unit': self.unit,
            'category': self.category,
            'source': self.source,
            'scraped_at': self.scraped_at.isoformat(),
            'url': self.url,
            'image_url': self.image_url,
            'description': self.description,
        }
