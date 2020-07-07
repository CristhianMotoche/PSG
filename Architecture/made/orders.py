from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass(frozen=True)
class OrderLines:
    orderid: str
    sku: str
    qty: int


@dataclass
class Batch:
    ref: str
    sky: str
    qty: int
    eta: Optional[date]

    def allocate(self, line: OrderLine) -> None:
        self.available_qty = -= line.qty
