"""Illustrative examples that demonstrate the SOLID design principles."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Protocol


# Single Responsibility Principle -------------------------------------------------
@dataclass(frozen=True)
class OrderLine:
    sku: str
    quantity: int
    unit_price: float

    def total(self) -> float:
        return self.quantity * self.unit_price


def calculate_order_total(lines: Iterable[OrderLine]) -> float:
    """Compute the monetary total for an order without side effects."""

    return sum(line.total() for line in lines)


# Open/Closed Principle -----------------------------------------------------------
class DiscountStrategy(Protocol):
    def apply(self, subtotal: float) -> float:
        """Return the discounted total based on the given subtotal."""


class NoDiscount:
    def apply(self, subtotal: float) -> float:
        return subtotal


class PercentageDiscount:
    def __init__(self, percent: float) -> None:
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        self._percent = percent

    def apply(self, subtotal: float) -> float:
        return subtotal * (1 - self._percent / 100)


# Liskov Substitution & Interface Segregation ------------------------------------
class Notifier(Protocol):
    def send(self, message: str) -> None:
        ...


class SMSNotifier:
    def send(self, message: str) -> None:
        print(f"SMS: {message}")


class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"Email: {message}")


# Dependency Inversion Principle --------------------------------------------------
class PaymentGateway(Protocol):
    def charge(self, amount: float) -> None:
        ...


class PaymentService:
    def __init__(self, gateway: PaymentGateway, notifier: Notifier) -> None:
        self._gateway = gateway
        self._notifier = notifier

    def checkout(self, lines: Iterable[OrderLine], discount: DiscountStrategy) -> float:
        subtotal = calculate_order_total(lines)
        total = discount.apply(subtotal)
        self._gateway.charge(total)
        self._notifier.send(f"Charged ${total:.2f}")
        return total


class FakeGateway:
    """Test double that records charges without making external calls."""

    def __init__(self) -> None:
        self.last_charge: float | None = None

    def charge(self, amount: float) -> None:
        self.last_charge = amount


__all__ = [
    "OrderLine",
    "calculate_order_total",
    "DiscountStrategy",
    "NoDiscount",
    "PercentageDiscount",
    "Notifier",
    "SMSNotifier",
    "EmailNotifier",
    "PaymentGateway",
    "PaymentService",
    "FakeGateway",
]
