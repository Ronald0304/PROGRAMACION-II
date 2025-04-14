class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1

class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1

if __name__ == "__main__":
    obj = D(1, 2, 3)
    print(f"Antes: x={obj.x}, y={obj.y}, z={obj.z}")
    obj.incrementaXYZ()
    print(f"Después de incrementaXYZ: x={obj.x}, y={obj.y}, z={obj.z}")
    obj.incrementaXZ()
    print(f"Después de incrementaXZ: x={obj.x}, y={obj.y}, z={obj.z}")
    obj.incrementaYZ()
    print(f"Después de incrementaYZ: x={obj.x}, y={obj.y}, z={obj.z}")
    obj.incrementaZ()
    print(f"Después de incrementaZ: x={obj.x}, y={obj.y}, z={obj.z}")
