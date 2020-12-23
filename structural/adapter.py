class Data:
    def request(self):
        return "Some data"


class Adaptee:
    def special_request(self):
        return "!yegres si eman ym olleH"


class Adapter(Data):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapted {self.adaptee.special_request()[::-1]}"


print(Adapter(Adaptee()).request())