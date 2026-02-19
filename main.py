from data.sample_health_data import generate_sample_data
from scaledown.compression import scale_down
from scaledown.anomaly import detect_anomalies
from agents.exercise_agent import exercise_agent
from evaluation.metrics import compression_ratio

raw = generate_sample_data()
scaled = scale_down(raw)

print("Compression:", compression_ratio(raw, scaled), "%")
print("Anomalies:", detect_anomalies(scaled))
print("Exercise advice:", exercise_agent(scaled))
