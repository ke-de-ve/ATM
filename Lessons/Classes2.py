class OurFirstClass:

    def say_hello(self):
        print('my first class!')

    def say_hi(self, name):
        print('Hi {}'.format(name))

print('Not a class')

obj = OurFirstClass()
print(obj.__class__)

obj.say_hello()
obj.say_hi('Everyone')