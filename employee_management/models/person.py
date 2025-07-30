class Person:
    def __init__(self, name, money=1000, mood="happy", health_rate=100):
        self.name = name
        self._money = money
        self._mood = mood
        self._health_rate = health_rate

    @property
    def health_rate(self):
        return self._health_rate

    @health_rate.setter
    def health_rate(self, value):
        if 0 <= value <= 100:
            self._health_rate = value
        else:
            raise ValueError("Health rate must be between 0 and 100")

    def sleep(self, hours):
        if hours == 7:
            self._mood = "happy"
        elif hours < 7:
            self._mood = "tired"
        else:
            self._mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self._money -= (items * 10)
