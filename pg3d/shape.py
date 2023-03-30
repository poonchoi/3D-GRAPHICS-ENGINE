class Shape:
    def __init__(self, app, size=1, center=[0, 0, 0]):
        if not isinstance(center, list) and not isinstance(center, tuple):
            raise Exception("center must be list or tuple")

        if not isinstance(size, float) and not isinstance(size, int):
            raise Exception("size must be int or float")

        if len(center) != 3:
            raise Exception("center must have 3 values")

        self.app = app
        self._center = center
        self._size = size
