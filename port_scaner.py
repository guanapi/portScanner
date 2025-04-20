import socket
import argparse


def scan_ports(host, ports):
    print(f"Scanning ports on {ports}...")
    all_ports = []
    try:
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                port = int(port)
                result = sock.connect_ex((host, port))

                if result == 0:
                    all_ports.append(f"Port {port} is open")
                else:
                    all_ports.append(f"Port {port} is closed")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    for port in all_ports:
        if "closed" in port:
            continue
        else:
            print(port)
    print("Port scan completed.")

def clean_ports(string_ports):
    cleaned_ports = []
    
    for port in string_ports.split(","):
        port = port.strip()
        if "-" in port:
            start, end = port.split("-")
            cleaned_ports.extend(range(int(start), int(end) + 1))
        else:
            cleaned_ports.append(int(port))
    print(f"Cleaned ports: {cleaned_ports}")
    return sorted(cleaned_ports)
# Arguments

parser = argparse.ArgumentParser(description="Port Scanner")
parser.add_argument("-t", "--target", required=True, help="Target IP address")
parser.add_argument("-p", "--ports", default= "1-1024", help="Comma-separated list of ports to scan")
args = parser.parse_args()


ports = clean_ports(args.ports)
scan_ports(args.target, ports)
# Example usage:


