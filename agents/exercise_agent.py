def exercise_agent(states):
    latest = states[-1]

    if "sleep_debt" in latest.flags:
        return "Recovery workout recommended"

    if latest.avg_steps < 5000:
        return "Increase daily activity"

    return "Normal training plan"
