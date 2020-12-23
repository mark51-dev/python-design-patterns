from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "<p>Some text!</p>"


class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component


class ConcreteDecorator(Decorator):
    def operation(self):
        return f"<div>{self._component.operation()}</div>"


class ConcreteDecorator2(Decorator):
    def operation(self):
        return f"<body>{self._component.operation()}</body>"


def client_code(component: Component):
    print(f"Result: {component.operation()}")


if __name__ == "__main__":
    simple = ConcreteComponent()
    client_code(simple)

    decorated = ConcreteDecorator(simple)
    decorated2 = ConcreteDecorator(decorated)
    decorated3 = ConcreteDecorator2(decorated2)

    client_code(decorated3)