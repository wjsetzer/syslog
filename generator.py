#! /usr/bin/env python

import random
import sys
import time

import syslog

if __name__ == '__main__':

  host = sys.argv[1]
  port = int(sys.argv[2])
  
  while True:
    level = random.choice(list(syslog.LEVEL.keys()))
    facility = random.choice(list(syslog.FACILITY.keys()))

    syslog.syslog(f"This is a syslog of LEVEL {level} and FACILITY {facility}", level, facility, (host, port))

    time.sleep(1)

