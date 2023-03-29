class Shape:
    def __init__(self, app, size=1, center=[0, 0, 0]):
        self.app = app

        self._center = center
        self._size = size
