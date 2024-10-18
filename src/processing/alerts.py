from config.config import Config

class AlertSystem:
    def __init__(self):
        self.threshold = Config.ALERT_THRESHOLD
        self.consecutive_count = Config.CONSECUTIVE_ALERTS
        self.alert_counts = {}

    def check_alert(self, data):
        city = data['city']
        temp = data['temp']

        if temp > self.threshold:
            if city not in self.alert_counts:
                self.alert_counts[city] = 1
            else:
                self.alert_counts[city] += 1

            if self.alert_counts[city] >= self.consecutive_count:
                self.trigger_alert(city, temp)
        else:
            self.alert_counts[city] = 0

    def trigger_alert(self, city, temp):
        print(f"ALERT: Temperature in {city} has exceeded {self.threshold}°C for {self.consecutive_count} consecutive updates. Current temperature: {temp}°C")
        # Here you could implement email notifications or other alert mechanisms