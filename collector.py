#!/usr/bin/env python3
import json, time, random, os

IPS = ["192.168.1.15", "10.0.0.5", "203.0.113.45", "198.51.100.77"]
EVENTS = ["login_success", "login_failed", "file_access", "network_scan"]
os.makedirs("logs", exist_ok=True)
STOP_FILE = os.path.join(os.getcwd(), "collector.stop")
LOG_FILE = os.path.join("logs", "logs.json")

def main_loop():
    while True:
        if os.path.exists(STOP_FILE):
            print("Collector stopping...")
            break
        log = {
            "timestamp": time.time(),
            "src_ip": random.choice(IPS),
            "event": random.choice(EVENTS)
        }
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log) + "\n")
        time.sleep(1)

if __name__ == "__main__":
    main_loop()