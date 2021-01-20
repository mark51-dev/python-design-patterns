# from abc import ABC, abstractmethod
#
#
# class Abstraction:
#     def __init__(self, implementation):
#         self.implementation = implementation
#
#     def operation(self):
#         return (f"Abstraction: Base operation with:\n"
#                 f"{self.implementation.operation_implementation()}")
#
#
# class ExtendedAbstraction(Abstraction):
#     def operation(self):
#         return (f"ExtendedAbstraction: Extended operation with:\n"
#                 f"{self.implementation.operation_implementation()}")
#
#
# class Implementation(ABC):
#     @abstractmethod
#     def operation_implementation(self):
#         pass
#
#
# class ConcreteImplementationA(Implementation):
#     def operation_implementation(self):
#         return "ConcreteImplementationA: Here's the result on the platform A."
#
#
# class ConcreteImplementationB(Implementation):
#     def operation_implementation(self):
#         return "ConcreteImplementationB: Here's the result on the platform B."
#
#
# def client_code(abstraction: Abstraction):
#     print(abstraction.operation(), end="")
#
#
# if __name__ == "__main__":
#     implementation = ConcreteImplementationA()
#     abstraction = Abstraction(implementation)
#     client_code(abstraction)
#
#     print("\n")
#
#     implementation = ConcreteImplementationB()
#     abstraction = ExtendedAbstraction(implementation)
#     client_code(abstraction)


from abc import ABC, abstractmethod


# Abstract Interface (aka Handle) used by the client
class Website(ABC):

    def __init__(self, implementation):
        # encapsulate an instance of a concrete implementation class
        self._implementation = implementation

    def __str__(self):
        return 'Interface: {}; Implementation: {}'.format(
            self.__class__.__name__, self._implementation.__class__.__name__)

    @abstractmethod
    def show_page(self):
        pass


class FreeWebsite(Website):

    def show_page(self):
        ads = self._implementation.get_ads()
        text = self._implementation.get_excerpt()
        call_to_action = self._implementation.get_call_to_action()
        print(ads)
        print(text)
        print(call_to_action)
        print('')


class PaidWebsite(Website):

    def show_page(self):
        text = self._implementation.get_article()
        print(text)
        print('')


class Implementation(ABC):

    def get_excerpt(self):
        return 'excerpt from the article'

    def get_article(self):
        return 'full article'

    def get_ads(self):
        return 'some ads'

    @abstractmethod
    def get_call_to_action(self):
        pass


class ImplementationA(Implementation):

    def get_call_to_action(self):
        return 'Pay 10 $ a month to remove ads'


class ImplementationB(Implementation):

    def get_call_to_action(self):
        return 'Remove ads with just 10 $ a month'


def main():
    a_free = FreeWebsite(ImplementationA())
    print(a_free)
    a_free.show_page()  # the client interacts only with the interface

    b_free = FreeWebsite(ImplementationB())
    print(b_free)
    b_free.show_page()

    a_paid = PaidWebsite(ImplementationA())
    print(a_paid)
    a_paid.show_page()

    b_paid = PaidWebsite(ImplementationB())
    print(b_paid)
    b_paid.show_page()


if __name__ == '__main__':
    main()