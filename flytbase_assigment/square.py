#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(2)

print 'take-off upto 5m altitude'
drone.take_off(5)

print 'drone positing at point A. among the ABCD square'

print 'drone moving towards side upto 6.5m distance in ABCD square at 5m altitude'

print 'drone positing at point B. among the ABCD square'
drone.position_set(6.5, 0, 0, yaw=1.0472, relative=True)

print 'drone positing at point C. among the ABCD square'
drone.position_set(0, 6.5, 0, relative=True)

print 'drone positing at point D. among the ABCD square'
drone.position_set(-6.5, 0, 0, relative=True)

print 'drone posting back to point A from point D. among the ABCD square'
drone.position_set(0, -6.5, 0, relative=True)

print 'mode landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()