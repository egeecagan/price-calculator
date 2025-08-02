class Measurements:
    def __init__(self, x, y, z, d):
        # init runs the property functions under the hood
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("x (length) must be greater than zero.")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("y (width) must be greater than zero.")
        self._y = value
    
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if value <= 0:
            raise ValueError("z (height) must be greater than zero.")
        self._z = value

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        if value <= 0:
            raise ValueError("d (density) must be greater than zero.")
        self._d = value

    def __repr__(self):
        return f"Measurements(x={self.x}, y={self.y}, z={self.z}, d={self.d})"

    def calculate_volume(self):
        return self.x * self.y * self.z

    def calculate_mass(self, volume):
        return volume * self.d
