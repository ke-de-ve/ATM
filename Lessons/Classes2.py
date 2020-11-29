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


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '(%d, %d, %d)' % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print("my point is ",my_point)