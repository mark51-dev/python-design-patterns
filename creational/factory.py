from abc import ABC, abstractmethod
import random


class AbsFactory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def do_some(self):
        return f"Car {self.factory_method().operation()} created"


class Audi(AbsFactory):
    def factory_method(self):
        rnd = random.randint(0, 15)
        if rnd == 0:
            return ProductAudiQ3()
        elif rnd > 7:
            return ProductAudiS7()
        else:
            return ProductAudiTT()
##fdsfdsf

class AbsProduct(ABC):
    @abstractmethod
    def operation(self):
        pass


class ProductAudiTT(AbsProduct):
    def operation(self):
        return "audi TT"


class ProductAudiQ3(AbsProduct):
    def operation(self):
        return "audi Q3"


class ProductAudiS7(AbsProduct):
    def operation(self):
        return "audi S7"


def run_code(factory: AbsFactory):
    print(f"Car production started \n{factory.do_some()}")


print("start")
run_code(Audi())
run_code(Audi())
run_code(Audi())
run_code(Audi())
