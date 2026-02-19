import time

def compression_ratio(raw, scaled):
    return round((1 - len(scaled) / len(raw)) * 100, 2)

def latency_test(data):
    time.sleep(len(data) * 0.0005)
