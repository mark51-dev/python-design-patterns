from abc import ABC, abstractmethod
import time


class Requester(ABC):
    @abstractmethod
    def request(self):
        pass


class RealRequest(Requester):
    def request(self):
        print("Connecting to server")


class Proxy(Requester):
    def __init__(self, login_to_server):
        self._login_to_server = login_to_server

    def request(self):
        if self.find_best_proxy():
            self._login_to_server.request()
            self.log_success()

    def find_best_proxy(self):
        print("Looking for best proxy for you!")
        time.sleep(1)
        print("Proxy found")
        return True

    def log_success(self):
        print("You logged in to server")


Proxy(RealRequest()).request()