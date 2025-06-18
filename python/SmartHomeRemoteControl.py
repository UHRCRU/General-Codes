from abc import ABC, abstractmethod

# --- Command Interface ---
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        pass

# --- Receiver Classes ---
class Light:
    def __init__(self, location="Generic"):
        self.location = location
        self.state = "off"

    def on(self):
        self.state = "on"
        print(f"{self.location} Light is ON")

    def off(self):
        self.state = "off"
        print(f"{self.location} Light is OFF")

class Fan:
    def __init__(self, location="Generic"):
        self.location = location
        self.speed = "off"

    def set_speed(self, speed):
        self.speed = speed
        print(f"{self.location} Fan is set to {self.speed.upper()}")

# --- Light Commands ---
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# --- Fan Commands ---
class FanHighCommand(Command):
    def __init__(self, fan):
        self.fan = fan
        self.prev_speed = "off"

    def execute(self):
        self.prev_speed = self.fan.speed
        self.fan.set_speed("high")

    def undo(self):
        self.fan.set_speed(self.prev_speed)

class FanMediumCommand(Command):
    def __init__(self, fan):
        self.fan = fan
        self.prev_speed = "off"

    def execute(self):
        self.prev_speed = self.fan.speed
        self.fan.set_speed("medium")

    def undo(self):
        self.fan.set_speed(self.prev_speed)

class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan
        self.prev_speed = "off"

    def execute(self):
        self.prev_speed = self.fan.speed
        self.fan.set_speed("off")

    def undo(self):
        self.fan.set_speed(self.prev_speed)

# --- Remote Control Invoker ---
class RemoteControl:
    def __init__(self):
        self._buttons = {}
        self._last_command = None

    def set_command(self, button_name, command):
        self._buttons[button_name] = command

    def press_button(self, button_name):
        command = self._buttons.get(button_name)
        if command:
            command.execute()
            self._last_command = command
        else:
            print(f"No command assigned to button '{button_name}'.")

    def press_undo(self):
        if self._last_command:
            print("Undoing last command...")
            self._last_command.undo()
        else:
            print("Nothing to undo.")

# --- Text-based Interface ---
def show_menu():
    print("\n--- Smart Home Remote ---")
    print("A: Living Room Light ON")
    print("B: Living Room Light OFF")
    print("C: Kitchen Light ON")
    print("D: Kitchen Light OFF")
    print("E: Fan HIGH")
    print("F: Fan MEDIUM")
    print("G: Fan OFF")
    print("U: UNDO last command")
    print("Q: Quit")

def main():
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    bedroom_fan = Fan("Bedroom")

    remote = RemoteControl()

    # Assign buttons
    remote.set_command("A", LightOnCommand(living_room_light))
    remote.set_command("B", LightOffCommand(living_room_light))
    remote.set_command("C", LightOnCommand(kitchen_light))
    remote.set_command("D", LightOffCommand(kitchen_light))
    remote.set_command("E", FanHighCommand(bedroom_fan))
    remote.set_command("F", FanMediumCommand(bedroom_fan))
    remote.set_command("G", FanOffCommand(bedroom_fan))

    while True:
        show_menu()
        choice = input("Press a button: ").strip().upper()
        if choice == "Q":
            print("Exiting Smart Home...")
            break
        elif choice == "U":
            remote.press_undo()
        else:
            remote.press_button(choice)

if __name__ == "__main__":
    main()
