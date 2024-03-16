
#problem statement: Create a demo app by following the FlytBase documentation to make the drone takeoff at 10m, move in a triangle trajectory of side lengt$

#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation cla$

time.sleep(2)

print 'mode takeoff upto 10m altitude'
drone.take_off(10.0)
print 'drone reached an altitude of 10m'

print ' drone moving towards side upto 10m distance in ABC triangle at 10m altitude '

# h^2=p^2+b^2, here the square root of sum of square of p=8m and b=6m
# gives us the desired side length of 10m.
drone.position_set(8.0, 6.0, 0, relative=True)

print ' drone from point B to C. among the ABC triangle
drone.position_set(-8.0, 6.0, 0, relative=True)

print ' drone from point C to A. among the ABC triangle
drone.position_set(0, -10, 0, relative=True)

print ' mode landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()