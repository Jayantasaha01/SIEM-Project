#!/usr/bin/env python3
import json, time
from parser import parse_logs

THRESHOLD_FAILED_LOGINS = 3


def detect_threats(logs):
    events = []
    failed = {}

    for log in logs:
        ip = log.get("src_ip")
        event = log.get("event")

        if event == "login_failed":
            failed[ip] = failed.get(ip, 0) + 1
            if failed[ip] >= THRESHOLD_FAILED_LOGINS:
                events.append({
                    "timestamp": time.time(),
                    "src_ip": ip,
                    "alert": "Brute-force login attempt detected"
                })
    return events

if __name__ == "__main__":
    logs = parse_logs("logs/sample_logs.json")
    events = detect_threats(logs)
    with open("events.json", "w") as f:
        json.dump(events, f, indent=2)
    print(f"Detected {len(events)} security events.")
