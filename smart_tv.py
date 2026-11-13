class TVIsOffError(Exception):
    pass


class SmartTV:
    ALLOWED_APPS = ("YouTube", "Netflix", "Spotify")

    def __init__(self):
        self.is_on = False
        self.volume = 20
        self.channel = 1
        self.current_app = None

    def _ensure_on(self):
        if not self.is_on:
            raise TVIsOffError("Turn the TV on first.")

    def power_on(self):
        self.is_on = True

    def power_off(self):
        self.is_on = False
        self.current_app = None

    def set_volume(self, level):
        self._ensure_on()

        if isinstance(level, int) and 0 <= level <= 100:
            self.volume = level
        else:
            raise ValueError(f"Level {level} is unacceptable.")

    def change_channel(self, number):
        self._ensure_on()

        if isinstance(number, int) and 1 <= number <= 999:
            self.channel = number
        else:
            raise ValueError(f"Channel {number} is invalid.")

    def launch_app(self, name):
        self._ensure_on()

        if name in self.ALLOWED_APPS:
            self.current_app = name
        else:
            raise ValueError(f"The app called {name} is not allowed.")

    def __str__(self):
        return f"Is on: {self.is_on}, volume: {self.volume}, channel: {self.channel}, current app: {self.current_app}."


if __name__ == "__main__":
    tv1 = SmartTV()
    print("# Initial.", tv1)

    tv1.power_on()
    tv1.launch_app("YouTube")
    tv1.set_volume(50)
    tv1.change_channel(112)

    print("# After correct changes.", tv1)

    tv1.power_off()
    print("# Power off.", tv1)
