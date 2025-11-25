# SIEM Log Analysis & Incident Detection

## Purpose
Simulate and detect suspicious authentication events using synthetic logs, Splunk queries, and a simple incident report.

## Contents
- logs/sample_syslog.log
- scripts/generate_logs.py
- queries/splunk_searches.txt
- queries/azure_kql_queries.txt
- notebooks/analysis.ipynb
- incident_report.md

## How to run (local)
1. `python3 scripts/generate_logs.py` to create logs.
2. Open `notebooks/analysis.ipynb` to run analysis.
3. Load `logs/sample_syslog.log` into Splunk or Sentinel and apply the queries in `queries/`.

## Resume Reference
See resume: ``

## Contact
Jayanta Saha — jayanta.saha0010@gmail.com
