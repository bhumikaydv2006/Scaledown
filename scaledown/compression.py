import statistics
from scaledown.models import HealthState

def scale_down(records, window=7):
    compressed = []

    for i in range(0, len(records), window):
        chunk = records[i:i+window]

        steps = [r.steps for r in chunk]
        hr = [r.avg_hr for r in chunk]
        sleep = [r.sleep_hours for r in chunk]

        trend = "stable"
        if sleep[-1] < sleep[0] - 0.5:
            trend = "declining"
        elif sleep[-1] > sleep[0] + 0.5:
            trend = "improving"

        flags = []
        if sum(sleep) / len(sleep) < 6:
            flags.append("sleep_debt")
        if max(hr) > 100:
            flags.append("high_hr")

        compressed.append(
            HealthState(
                period=f"{chunk[0].day} → {chunk[-1].day}",
                avg_steps=int(sum(steps) / len(steps)),
                avg_hr=round(sum(hr) / len(hr), 1),
                avg_sleep=round(sum(sleep) / len(sleep), 1),
                trend=trend,
                flags=flags
            )
        )

    return compressed
