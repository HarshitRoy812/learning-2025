"""Python practice modules for the Learning 2025 curriculum."""

from .dataset_summary import compute_numeric_summary, load_csv
from .solid_design_principles import (
    DiscountStrategy,
    EmailNotifier,
    FakeGateway,
    NoDiscount,
    Notifier,
    OrderLine,
    PaymentGateway,
    PaymentService,
    PercentageDiscount,
    SMSNotifier,
    calculate_order_total,
)

__all__ = [
    "compute_numeric_summary",
    "load_csv",
    "DiscountStrategy",
    "EmailNotifier",
    "FakeGateway",
    "NoDiscount",
    "Notifier",
    "OrderLine",
    "PaymentGateway",
    "PaymentService",
    "PercentageDiscount",
    "SMSNotifier",
    "calculate_order_total",
]
