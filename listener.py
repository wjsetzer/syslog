#! /usr/bin/env python

import socket
import sys

def main(argv: list):

  host = argv[1]
  port = int(argv[2])

  with socket.socket(type=socket.SOCK_DGRAM) as s:
    s.bind((host, port))

    while True:
      d = s.recv(1024)
      if not d:
        break
      print(d)
  
if __name__ == '__main__':
  main(sys.argv)
