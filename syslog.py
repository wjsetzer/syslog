#! /usr/bin/env python

import socket
import sys

FACILITY = {
  'kern'     : 0,
  'user'     : 1,
  'mail'     : 2,
  'daemon'   : 3,
  'auth'     : 4,
  'syslog'   : 5,
  'lpr'      : 6,
  'news'     : 7,
  'uucp'     : 8,
  'cron'     : 9,
  'authpriv' : 10,
  'ftp'      : 11,
  'ntp'      : 12,
  'security' : 13,
  'console'  : 14,
  'solaris-cron' : 15,
  'local0'   : 16,
  'local1'   : 17,
  'local2'   : 18,
  'local3'   : 19,
  'local4'   : 20,
  'local5'   : 21,
  'local6'   : 22,
  'local7'   : 23,
}

LEVEL = {
  'emerg'   : 0,
  'alert'   : 1,
  'crit'    : 2,
  'err'     : 3,
  'warning' : 4,
  'notice'  : 5,
  'info'    : 6,
  'debug'   : 7,
}

def syslog(message, level='notice', facility='daemon', host=('localhost', 514)):

  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    data = f"<{LEVEL[level] + FACILITY[facility]*8}>{message}".encode()
    sock.sendto(data, host)

def main(argv: list):

  host = argv[1]
  port = int(argv[2])
  level = argv[3].lower()
  facility = argv[4].lower()
  message = argv[5]
  
  syslog(message, level, facility, host, port)
  

if __name__ == '__main__':
  main(sys.argv)
