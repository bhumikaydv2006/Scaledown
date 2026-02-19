import statistics

def detect_anomalies(states):
    alerts = []
    baseline_hr = statistics.mean(s.avg_hr for s in states)

    for s in states:
        if s.avg_hr > baseline_hr + 10:
            alerts.append(f"High HR anomaly: {s.period}")
        if "sleep_debt" in s.flags:
            alerts.append(f"Sleep debt detected: {s.period}")

    return alerts
