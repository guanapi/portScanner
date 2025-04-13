import socket
import argparse


def scan_ports(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)
            result = sock.connect_ex((host, port))

            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


scan_ports("164.234.23.1", 80)

