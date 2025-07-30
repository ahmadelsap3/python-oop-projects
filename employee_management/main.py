from models import Car, Employee, Office

def main():
    # Create Samy's car
    fiat128 = Car("Fiat 128")

    # Create Samy as an employee
    samy = Employee("Samy", 1, "samy@iti.com", 5000, fiat128, 20)

    # Create ITI office
    iti = Office("ITI Smart Village")

    # Hire Samy
    iti.hire(samy)

    # Simulate Samy's daily routine
    samy.sleep(7)  # Normal sleep
    samy.eat(3)    # Healthy eating
    
    # Samy drives to work
    departure_time = 8  # 8:00 AM
    samy.drive(samy.distance_to_work, 60)  # 60 km/h
    
    # Check if Samy is late
    is_late = iti.check_lateness(samy.id, departure_time)
    print(f"Samy is {'late' if is_late else 'on time'}")

if __name__ == "__main__":
    main()
