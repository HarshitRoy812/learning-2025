# Module 8: SOLID Design Principles

## Overview
This module strengthens learners' ability to design maintainable Python systems by applying the SOLID object-oriented design principles. Through architecture discussions, code reviews, and refactoring exercises, learners develop intuition for balancing extensibility with simplicity.

## Week 1: Single Responsibility & Open/Closed Principles
Focus: Structuring classes so that each has one reason to change while remaining open for extension.

### Guided Reading & Discussion
- Explore historical context of SOLID and its relevance to modern Python projects.
- Compare tightly coupled code with modular alternatives.
- Analyze open/closed violations in legacy services and draft refactoring approaches.

### Lab: Refactoring a Reporting Service
Learners decouple data access, transformation, and presentation layers in a reporting microservice. They implement strategy objects to support new output formats without modifying existing code.

```python
from typing import Protocol

class ReportFormatter(Protocol):
    def format(self, metrics: dict) -> str:
        ...

class TextFormatter:
    def format(self, metrics: dict) -> str:
        return "\n".join(f"{key}: {value}" for key, value in metrics.items())

class JSONFormatter:
    def format(self, metrics: dict) -> str:
        import json
        return json.dumps(metrics)

class ReportGenerator:
    def __init__(self, formatter: ReportFormatter) -> None:
        self._formatter = formatter

    def generate(self, metrics: dict) -> str:
        return self._formatter.format(metrics)

print(ReportGenerator(TextFormatter()).generate({"uptime": 99.9}))
print(ReportGenerator(JSONFormatter()).generate({"uptime": 99.9}))
```

## Week 2: Liskov Substitution & Interface Segregation Principles
Focus: Designing polymorphic APIs that remain substitutable and tailored to consumer needs.

### Guided Reading & Discussion
- Examine inheritance hierarchies that break substitutability.
- Evaluate Python-specific nuances: duck typing, abstract base classes, and protocols.
- Identify overgrown interfaces and practice splitting them into focused roles.

### Lab: Device Control Interfaces
Learners refactor a hardware control SDK. They replace a monolithic interface with specialized protocols and validate substitutability using unit tests and static typing.

```python
from typing import Protocol

class Switchable(Protocol):
    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...

class Dimmable(Switchable, Protocol):
    def set_brightness(self, level: int) -> None:
        ...

class SmartBulb:
    def __init__(self) -> None:
        self._is_on = False
        self._brightness = 0

    def turn_on(self) -> None:
        self._is_on = True

    def turn_off(self) -> None:
        self._is_on = False

    def set_brightness(self, level: int) -> None:
        if not 0 <= level <= 100:
            raise ValueError("Brightness must be between 0 and 100")
        self._brightness = level
```

## Week 3: Dependency Inversion Principle
Focus: Inverting dependencies to decouple high-level policies from low-level details.

### Guided Reading & Discussion
- Study dependency inversion in layered architectures and hexagonal design.
- Contrast service locator, dependency injection, and factories in Python ecosystems.
- Review real-world case studies of dependency inversion within data pipelines.

### Lab: Notification Service Architecture
Learners build a notification service that coordinates multiple channels via dependency injection and adapters. They write tests using fakes to validate orchestration logic independently from infrastructure.

```python
from typing import Iterable, Protocol

class Notifier(Protocol):
    def send(self, message: str) -> None:
        ...

class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotifier:
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

class NotificationService:
    def __init__(self, notifiers: Iterable[Notifier]) -> None:
        self._notifiers = list(notifiers)

    def broadcast(self, message: str) -> None:
        for notifier in self._notifiers:
            notifier.send(message)

service = NotificationService([EmailNotifier(), SMSNotifier()])
service.broadcast("SOLID keeps systems adaptable!")
```

## Week 4: Integrated Case Study & Assessment
Focus: Synthesizing SOLID into a cohesive codebase and reflecting on architectural trade-offs.

### Project Brief
Learners audit an event-driven analytics platform, refactoring hotspots that violate SOLID. They apply unit tests, static analysis, and architectural decision records to document the changes.

### Assessment
- Whiteboard walkthrough of SOLID trade-offs and when to compromise.
- Code review evaluating adherence to principles, testability, and readability.
- Reflection essay on how SOLID supports long-term maintainability in analytics teams.
