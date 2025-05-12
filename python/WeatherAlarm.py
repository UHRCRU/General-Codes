from abc import ABC, abstractmethod
from typing import List, Dict

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify_observers(self) -> None:
        pass

class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 1013.25  
    
    def register_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[WeatherStation] Registered new observer: {type(observer).__name__}")
    
    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[WeatherStation] Removed observer: {type(observer).__name__}")
    
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"\n[WeatherStation] Updating measurements: "
              f"{temperature}°C, {humidity}%, {pressure}hPa")
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

class DisplayDevice(ABC):
    @abstractmethod
    def show(self, data: Dict[str, float]) -> None:
        pass

class PhoneDisplay(Observer):
    def __init__(self, display: DisplayDevice):
        self._display = display  
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._display.show({
            "type": "Phone",
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure
        })

class LEDDisplay(Observer):
    def __init__(self, display: DisplayDevice):
        self._display = display  
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._display.show({
            "type": "LED",
            "temperature": temperature,
            "humidity": humidity
        })

class AlarmSystem(Observer):
    def __init__(self, alert_thresholds: Dict[str, float]):
        self.thresholds = alert_thresholds  
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        alerts = []
        if temperature > self.thresholds["max_temp"]:
            alerts.append(f"High temperature: {temperature}°C")
        if humidity > self.thresholds["max_humidity"]:
            alerts.append(f"High humidity: {humidity}%")
        
        if alerts:
            print(f"[AlarmSystem] ALERT! {' | '.join(alerts)}")
        else:
            print(f"[AlarmSystem] Conditions normal")

class ConsoleDisplay(DisplayDevice):
    def show(self, data: Dict[str, float]) -> None:
        print(f"[{data['type']}Display] Current weather: "
              f"{data['temperature']}°C, {data.get('humidity', 'N/A')}%")

class FancyLEDDisplay(DisplayDevice):
    def show(self, data: Dict[str, float]) -> None:
        print(f"=== LED Matrix Display ===")
        print(f"Temp: {data['temperature']}°C")
        print(f"Humidity: {data['humidity']}%")
        print("========================")

def main():
    weather_station = WeatherStation()
    
    console_display = ConsoleDisplay()
    led_matrix = FancyLEDDisplay()
    
    phone_app = PhoneDisplay(console_display)
    led_panel = LEDDisplay(led_matrix)
    alarm = AlarmSystem({
        "max_temp": 30.0,
        "max_humidity": 80.0
    })
    
    weather_station.register_observer(phone_app)
    weather_station.register_observer(led_panel)
    weather_station.register_observer(alarm)
    
    weather_station.set_measurements(22.5, 65.0, 1015.0)
    weather_station.set_measurements(32.0, 85.0, 1012.0)
    
    weather_station.remove_observer(led_panel)
    weather_station.set_measurements(18.0, 70.0, 1018.0)

if __name__ == "__main__":
    main()