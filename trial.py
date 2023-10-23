class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyClass(name='{self.name}')"

    def __str__(self):
        return f"Object of MyClass with name '{self.name}'"

obj = MyClass('example')
print(obj)        # 调用 obj.__str__() 方法，输出结果：Object of MyClass with name 'example'
print(repr(obj))  # 调用 obj.__repr__() 方法，输出结果：MyClass(name='example')

obj2 = MyClass('a')
print(obj2)  