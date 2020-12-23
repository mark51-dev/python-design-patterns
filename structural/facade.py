class Facade:
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1 or subsystem1()
        self._subsystem2 = subsystem2 or subsystem2()

    def operation(self):
        results = []
        results.append("Facade initialization")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("subsystems initialization")
        results.append(self._subsystem1.operationX())
        results.append(self._subsystem2.operationX())
        return "\n".join(results)


class Subsystem1:
    def operation1(self):
        return "Subsystem 1"

    def operationX(self):
        return "system 1 operation x"


class Subsystem2:
    def operation1(self):
        return "Subsystem 2"

    def operationX(self):
        return "system 2 operation x"


def run_code(facade):
    print(facade.operation())


run_code(Facade(Subsystem1(), Subsystem2()))