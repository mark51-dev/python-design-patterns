from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def add_processor(self):
        pass

    @abstractmethod
    def add_graphic_cart(self):
        pass

    @abstractmethod
    def add_ssd(self):
        pass


class PcBuilder(Builder):
    def __init__(self):
        self._product = PC()

    def reset(self):
        self._product = PC()

    def add_processor(self):
        self._product.add("Intel 4433")
        return self

    def add_graphic_cart(self):
        self._product.add("Gigabyte 760")
        return self

    def add_ssd(self):
        self._product.add("Samsung 512gb")
        return self

    def __str__(self):
        return self._product.list_parts()


class PC():
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Product parts: {', '.join(self.parts)}"


res = PcBuilder().add_processor().add_graphic_cart().add_ssd()
res2 = PcBuilder().add_graphic_cart().add_ssd().add_processor()
print(res)
print(res2)