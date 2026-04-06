import os
import csv
import socket
import time
from datetime import datetime
from plyer import notification

# Target DNS servers
TARGETS = {
    "Google_DNS": "8.8.8.8",
    "Cloudflare_DNS": "1.1.1.1",
    "Quad9_DNS": "9.9.9.9"
}
PORT = 53
TIMEOUT = 5
LATENCY_THRESHOLD = 100.0  # Alert if higher than 100ms

def send_chaski_alert(title, message):
    """Triggers a Windows Toast Notification for Chaski-Link."""
    notification.notify(
        title=f"Chaski-Link: {title}",
        message=message,
        app_name="Chaski-Link NPM",
        timeout=10
    )

def get_latency(host):
    start_time = time.perf_counter()
    try:
        with socket.create_connection((host, PORT), timeout=TIMEOUT) as sock:
            end_time = time.perf_counter()
            latency = (end_time - start_time) * 1000
            
            # High latency check
            if latency > LATENCY_THRESHOLD:
                send_chaski_alert("High Latency", f"{host} responded in {latency:.2f}ms")
                
            return f"{latency:.2f}ms"
    except (socket.timeout, Exception):
        send_chaski_alert("Runner Delayed", f"The messenger failed to reach {host}")
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
    
    print(f"Chaski-Link: Log updated at {timestamp}")

if __name__ == "__main__":
    main()