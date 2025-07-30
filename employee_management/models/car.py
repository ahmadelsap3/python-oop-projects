class Car:
    def __init__(self, name, fuel_rate=100, velocity=0):
        self.name = name
        self._fuel_rate = fuel_rate
        self._velocity = velocity

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            raise ValueError("Fuel rate must be between 0 and 100")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            raise ValueError("Velocity must be between 0 and 200")

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_consumption = (distance / 10) * 10  # 10% decrease every 10km
        if self.fuel_rate >= fuel_consumption:
            self.fuel_rate -= fuel_consumption
            self.stop(0)
            return True
        else:
            remaining_distance = distance - ((self.fuel_rate / 10) * 10)
            self.fuel_rate = 0
            self.stop(remaining_distance)
            return False

    def stop(self, remaining_distance=0):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Stopped: {remaining_distance}km remaining due to insufficient fuel")
        else:
            print("Arrived at destination")
