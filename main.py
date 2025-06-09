# main.py

import time
import math

from mta import LTrain
from helper import from_minutes

UPDATE_SEC = 5

# Morgan ave stop id = L14N or L14S
morganStop = LTrain("L14")

while True:
    N_times, S_times = morganStop.getNextTimes()
    print(f"Next Manhattan L: {from_minutes(N_times[0])}")
    print(f"Next Canarsie L: {from_minutes(S_times[0])}")
    time.sleep(UPDATE_SEC)
    