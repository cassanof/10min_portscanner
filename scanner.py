from time import sleep
import socket
import sys
import _thread

# Dumbest python scanner ever made in 10 minutes

openPorts = []

def main():
    if len(sys.argv) > 2:
        addr = sys.argv[1]
        portRange = parseRange()
    else:
        print("Please specify IP and port range in format: 1.1.1.1 20-80")
        exit(-1)

    scan(addr, portRange)


def handler(addr, port, lastPort):
    print(f"Scanning port: {port}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((addr, port))
    if res == 0:
        print(f"Port {port} is open!")
        openPorts.append(port)
    sock.close()
    if port == lastPort:
        print("Scan done! printing open ports!")
        for openPort in openPorts:
            print(f"*** {openPort}")

def scan(addr, portRange):
    print(f"Scanning: {addr} range: {str(portRange)}")

    for port in range(portRange[0], portRange[1]+1):
        _thread.start_new_thread(handler, (addr, port, portRange[1]))
        sleep(0.005)
    input() # keep it open

def parseRange():
    ports = sys.argv[2].split('-')
    return (int(ports[0]),int(ports[1]))

if __name__ == "__main__":
    main()
