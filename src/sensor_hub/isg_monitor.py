import time
import random

class ISGMonitor:
    """
    Monitors environmental conditions and personnel health status.
    """
    def __init__(self):
        self.thresholds = {
            "methane": 5.0, # percentage
            "co2": 1000,   # ppm
            "heart_rate_min": 50,
            "heart_rate_max": 120
        }
    
    def read_sensors(self):
        """
        Simulates reading from IoT sensors.
        """
        return {
            "methane": random.uniform(0.0, 6.0),
            "co2": random.randint(400, 1200),
            "heart_rate": random.randint(60, 130),
            "location": (random.uniform(36.0, 42.0), random.uniform(26.0, 45.0)) # Lat, Long
        }

    def check_safety(self, data):
        """
        Checks if sensor data exceeds safety thresholds.
        """
        alerts = []
        if data["methane"] > self.thresholds["methane"]:
            alerts.append(f"CRITICAL: High Methane Level detected: {data['methane']:.2f}%")
        if data["co2"] > self.thresholds["co2"]:
            alerts.append(f"WARNING: High CO2 Level detected: {data['co2']} ppm")
        if data["heart_rate"] > self.thresholds["heart_rate_max"] or data["heart_rate"] < self.thresholds["heart_rate_min"]:
             alerts.append(f"ALERT: Abnormal Heart Rate: {data['heart_rate']} bpm")
        
        return alerts

if __name__ == "__main__":
    monitor = ISGMonitor()
    print("Starting ISG Monitoring System...")
    try:
        while True:
            sensor_data = monitor.read_sensors()
            safety_alerts = monitor.check_safety(sensor_data)
            
            print(f"Reading: {sensor_data}")
            if safety_alerts:
                for alert in safety_alerts:
                    print(f"!!! {alert} !!!")
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
