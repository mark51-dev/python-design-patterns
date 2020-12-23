from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver, command1, command2):
        self._receiver = receiver
        self._command1 = command1
        self._command2 = command2

    def execute(self) -> None:
        print("Code execution complex command")
        self._receiver.do_something(self._command1)
        self._receiver.do_something_else(self._command2)


class Receiver:
    def do_something(self, a):
        print(f"Receiver working { a }", end="")

    def do_something_else(self, b):
        print(f"Receiver also working { b }", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before I begin?", end="")
        self._on_start.execute()

        print("Invoker: Does anybody want something done after I finish?", end="")
        self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Hehehehehehey"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "First", "Second"))
    invoker.do_something_important()