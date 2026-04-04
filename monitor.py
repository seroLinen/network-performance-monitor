import os
import csv
import socket
import time
from datetime import datetime

# The servers and the DNS port (53) we are monitoring
TARGETS = {
    "Google_DNS": "8.8.8.8",
    "Cloudflare_DNS": "1.1.1.1",
    "Quad9_DNS": "9.9.9.9"
}
PORT = 53
TIMEOUT = 5

def get_latency(host):
    """
    Measures latency using a TCP connection. 
    This bypasses GitHub's ICMP (ping) block.
    """
    start_time = time.perf_counter()
    try:
        # Create a socket and attempt to connect to Port 53
        with socket.create_connection((host, PORT), timeout=TIMEOUT) as sock:
            end_time = time.perf_counter()
            latency = (end_time - start_time) * 1000
            return f"{latency:.2f}ms"
    except (socket.timeout, Exception):
        return "Timeout/Error"

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp]
    headers = ["Timestamp"]

    for name, ip in TARGETS.items():
        headers.append(name)
        row.append(get_latency(ip))

    file_name = 'network_log.csv'
    file_exists = os.path.isfile(file_name)

    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(row)
    
    print(f"Log updated at {timestamp}")

if __name__ == "__main__":
    main()