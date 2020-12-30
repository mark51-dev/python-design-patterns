from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class Handler(AbstractHandler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class Admin(Handler):
    def handle(self, request):
        if request == "restart":
            return "Admin started restart server"
        else:
            return super().handle(request)


class Moderator(Handler):
    def handle(self, request):
        if request == "check_connection":
            return "Checking some basic info about client server"
        else:
            return super().handle(request)


class Support(Handler):
    def handle(self, request):
        if request == "reboot_router":
            return "Geting some information from client"
        else:
            return super().handle(request)


def run_code(handle):
    for item in ["check_connection", "reboot_router", "restart"]:
        print("Client who server doesnt work")
        result = handle.handle(item)
        if result:
           print(f"{result}")


if __name__ == "__main__":
    support = Support()
    moderator = Moderator()
    admin = Admin()

    support.set_next(moderator).set_next(admin)

    run_code(support)
