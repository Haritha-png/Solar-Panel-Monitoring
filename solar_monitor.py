import random
from datetime import datetime

# Threshold values
VOLTAGE_MIN = 10.0
VOLTAGE_MAX = 24.0
CURRENT_MAX = 5.0
TEMP_MAX = 60.0

def read_sensors():
    voltage = round(random.uniform(9.5, 25.0), 2)
    current = round(random.uniform(0.0, 6.0), 2)
    temperature = round(random.uniform(20.0, 70.0), 2)
    return voltage, current, temperature

def calculate_power(voltage, current):
    return round(voltage * current, 2)

def check_alerts(voltage, current, temperature):
    alerts = []
    if voltage < VOLTAGE_MIN:
        alerts.append("Low Voltage Alert")
    if voltage > VOLTAGE_MAX:
        alerts.append("High Voltage Alert")
    if current > CURRENT_MAX:
        alerts.append("Overcurrent Alert")
    if temperature > TEMP_MAX:
        alerts.append("Over Temperature Alert")
    return alerts

def generate_10_readings():
    readings = []
    for _ in range(10):
        voltage, current, temp = read_sensors()
        power = calculate_power(voltage, current)
        alerts = check_alerts(voltage, current, temp)
        status = " | ".join(alerts) if alerts else "OK"
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        readings.append({
            "time": now,
            "voltage": voltage,
            "current": current,
            "power": power,
            "temperature": temp,
            "status": status
        })
    return readings
