# Incident Report: Brute Force Detection (sample)

**Date:** 2025-11-25

## Overview
Detected brute-force attempts from IP 203.0.113.45 targeting web01.example.com.

## Timeline
- 2025-11-25T12:02Z - First failure observed
- 2025-11-25T12:06Z - >10 failures within 5 minutes

## Indicators of Compromise (IoCs)
- src_ip: 203.0.113.45
- username: unknown
- host: web01.example.com

## Actions taken
1. Blocked IP at perimeter firewall (pfSense rule)
2. Forced password resets for impacted accounts
3. Increased logging and created detection rule in Splunk/Sentinel

## Recommendations
- Implement rate limiting, MFA, and geoblocking for admin interfaces.
