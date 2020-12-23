from abc import ABC, abstractmethod
import time

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observable(Subject):
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()


class Observer(ABC):
    _number = 0

    @abstractmethod
    def update(self):
        pass


class Observer1(Observer):

    def update(self):
        self._number = self._number + 1
        print(f"Number +1 is {self._number}")


class Observer2(Observer):
    def update(self):
        self._number = self._number + 10
        print(f"Number +10 is {self._number}")


class Observer3(Observer):
    def update(self):
        self._number = self._number + 100
        print(f"Number +100 is {self._number}")


observable = Observable()
observer1 = Observer1()
observer2 = Observer2()
observer3 = Observer3()

observable.attach(observer1)
observable.attach(observer2)
observable.attach(observer3)

for i in range(1000):
    observable.notify()
    time.sleep(1)