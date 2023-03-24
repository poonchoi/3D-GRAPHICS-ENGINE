from pg3dFINAL import *

app = pg3d.App((1000, 700))
points = [[1, 1, 1], [-1, -1, 1], [-1, 1, 1], [1, -1, 1], 
          [1, 1, -1], [-1, -1, -1], [-1, 1, -1], [1, -1, -1], ]
classpoints = [pg3d.Point(app, i) for i in points]
app.run()