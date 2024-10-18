class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
x = MyClass()
x.i = 12
print(x.i)