class Office:
    employees_num = 0  # Class variable for number of employees across all offices

    def __init__(self, name):
        self.name = name
        self.employees = {}

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num

    def get_all_employees(self):
        return list(self.employees.values())

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)

    def hire(self, employee):
        self.employees[employee.id] = employee
        Office.employees_num += 1

    def fire(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            Office.employees_num -= 1

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        time_taken = distance / velocity
        arrival_hour = move_hour + time_taken
        return arrival_hour > target_hour

    def check_lateness(self, emp_id, move_hour):
        employee = self.get_employee(emp_id)
        if employee:
            is_late = self.calculate_lateness(9, move_hour, 
                                           employee.distance_to_work, 
                                           employee.last_driving_velocity)
            if is_late:
                self.deduct(emp_id, 10)
            else:
                self.reward(emp_id, 10)
            return is_late

    def deduct(self, emp_id, deduction):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary = max(1000, employee.salary - deduction)

    def reward(self, emp_id, reward):
        employee = self.get_employee(emp_id)
        if employee:
            employee.salary += reward
