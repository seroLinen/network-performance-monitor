import os
import csv
import subprocess
import platform
from datetime import datetime

# The servers you want to monitor
TARGETS = {
    "Google_DNS": "8.8.8.8",
    "Cloudflare_DNS": "1.1.1.1",
    "Quad9_DNS": "9.9.9.9"
}

def get_latency(host):
    # Determines if the OS is Windows or Linux/Mac to use correct ping flag
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    
    try:
        # Run the ping command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode()
        
        # Logic to extract the 'ms' value from the ping text
        if "time=" in output:
            # Typical format: "... time=15.2 ms ..."
            latency = output.split("time=")[1].split("ms")[0].strip()
            return f"{latency}ms"
        return "No Response"
    except Exception:
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