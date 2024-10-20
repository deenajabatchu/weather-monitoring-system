def check_alerts(temperature):
    threshold = 35  # Example threshold
    if temperature > threshold:
        print(f"Alert! Temperature exceeds {threshold}°C.")