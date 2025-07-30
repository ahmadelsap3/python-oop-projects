from .person import Person

class Employee(Person):
    def __init__(self, name, id, email, salary, car=None, distance_to_work=0):
        super().__init__(name)
        self.id = id
        self.car = car
        self.email = email
        self._salary = salary
        self.distance_to_work = distance_to_work
        self.last_driving_velocity = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            raise ValueError("Salary cannot be less than 1000")

    def work(self, hours):
        if hours == 8:
            self._mood = "happy"
        elif hours > 8:
            self._mood = "tired"
        else:
            self._mood = "lazy"

    def drive(self, distance, velocity):
        if self.car:
            self.last_driving_velocity = velocity
            return self.car.run(velocity, distance)
        else:
            raise ValueError("Employee doesn't have a car")

    def refuel(self, gas_amount=100):
        if self.car:
            self.car.fuel_rate = min(100, self.car.fuel_rate + gas_amount)
        else:
            raise ValueError("Employee doesn't have a car")

    def send_mail(self, to, subject, msg, receiver_name):
        print(f"""
        From: {self.email}
        To: {to}
        Subject: {subject}
        Hi {receiver_name},
        {msg}
        Thanks,
        {self.name}
        """)
