class ExampleClass:
    def __init__(self, value):
        self.__private_attr = value  

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, value):
        self.__private_attr = value

    def access_private_directly(self):
        return self._ExampleClass__private_attr

    private_attr = property(get_private_attr, set_private_attr)


obj = ExampleClass(5)

obj.private_attr = 15

print("Value through property:", obj.private_attr)

print("Direct access to a private attribute:", obj.access_private_directly())
