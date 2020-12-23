from abc import ABC, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def create_product_1(self):
        pass

    def create_product_2(self):
        pass


class FactoryProduct1(AbsFactory):
    def create_product_1(self):
        return Product1()

    def create_product_2(self):
        return AdvancedProduct1()


class FactoryProduct2(AbsFactory):
    def create_product_1(self):
        return Product2()

    def create_product_2(self):
        return AdvancedProduct2()


class Product(ABC):
    def operation(self):
        pass


class Product1(Product):
    def operation(self):
        return "Car 1"


class Product2(Product):
    def operation(self):
        return "Car 2"


class AdvancedProduct(ABC):
    def operation(self):
        pass

    def advanced_func(self, collaborator):
        pass


class AdvancedProduct1(Product2):
    def operation(self):
        return "Car 1"

    def advanced_func(self, collaborator):
        print("advanced func prod 1")
        return collaborator.operation()


class AdvancedProduct2(Product2):
    def operation(self):
        return "Car 2"

    def advanced_func(self, collaborator):
        print("advanced func prod 2")
        return collaborator.operation()


def run_code(factory: AbsFactory):
    op1 = factory.create_product_1()
    op2 = factory.create_product_2()
    print(op2.advanced_func(op1))
    print(op1.operation())

run_code(FactoryProduct1())