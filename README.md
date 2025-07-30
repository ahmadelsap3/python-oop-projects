# Python OOP Projects Collection

This repository contains three different Python projects demonstrating various Object-Oriented Programming concepts.

## Project Structure
```
.
├── multiple_inheritance/
│   └── multiple_inheritance.py     # Demonstrates multiple inheritance concept
├── website_opener/
│   └── website_opener.py          # Random website opener using standard library
└── employee_management/           # Main project implementing Samy's story
    ├── main.py                    # Entry point of the program
    └── models/
        ├── __init__.py           # Package initializer
        ├── person.py             # Person base class
        ├── car.py               # Car class implementation
        ├── employee.py          # Employee class (inherits from Person)
        └── office.py           # Office class implementation
```

## 1. Multiple Inheritance Example
Located in `multiple_inheritance/` folder, this project demonstrates Python's multiple inheritance using a simple animal hierarchy example. It shows how a class can inherit from multiple parent classes and the method resolution order (MRO).

### Output
```python
Pet Buddy created
Dog barks
MRO of Pet: (<class '__main__.Pet'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
```

## 2. Random Website Opener
Located in `website_opener/` folder, this project demonstrates the use of Python's standard library modules (`webbrowser` and `random`) to randomly select and open a website from a predefined list.

### Output
```
Opening https://www.python.org...
# Browser opens with the randomly selected website
```

## 3. Employee Management System (Samy's Story)
Located in `employee_management/` folder, this project implements a comprehensive story about an employee named Samy.

### The Story
Samy is an employee at ITI Smart Village who commutes daily (except weekends) using his Fiat 128 car. Here are the key points of the story:
- Samy lives 20 km away from ITI
- He must arrive before 9:00 AM to avoid being late
- His car's fuel consumption is tracked (10% decrease every 10km)
- His performance affects his salary (rewards/deductions based on attendance)

### Implementation Details

#### Person Class (`person.py`)
- Base class for human entities
- Manages basic human needs:
  - Sleep (affects mood: 7h→happy, <7h→tired, >7h→lazy)
  - Eat (affects health: 3 meals→100%, 2 meals→75%, 1 meal→50%)
  - Buy (each item costs 10 L.E)

#### Car Class (`car.py`)
- Represents vehicles with:
  - Fuel rate (0-100%)
  - Velocity (0-200 km/h)
  - Run/stop functionality
  - Fuel consumption tracking

#### Employee Class (`employee.py`)
- Inherits from Person
- Additional features:
  - Salary management
  - Car ownership
  - Email communication
  - Work schedule tracking

#### Office Class (`office.py`)
- Manages employee records
- Handles:
  - Hiring/firing
  - Attendance tracking
  - Salary adjustments
  - Employee count across all offices

### Example Run (from main.py)
```python
# Output when running main.py:
Arrived at destination
Samy is on time
```

This output shows that:
1. Samy successfully arrived at his destination (ITI)
2. He arrived before 9:00 AM (considering he left at 8:00 AM and took 20 minutes to travel 20km at 60km/h)

### Key Calculations
- Distance: 20 km
- Speed: 60 km/h
- Travel time: 20 km ÷ 60 km/h = 1/3 hour (20 minutes)
- Departure: 8:00 AM
- Arrival: 8:20 AM (before 9:00 AM → on time)
- Fuel consumption: 20% (10% per 10km)

## Requirements
- Python 3.6 or higher
- Standard library modules only (no additional dependencies needed)

## How to Run
1. Clone the repository
2. Navigate to the desired project folder
3. Run the main script:
```bash
# For employee management system:
python employee_management/main.py

# For multiple inheritance example:
python multiple_inheritance/multiple_inheritance.py

# For website opener:
python website_opener/website_opener.py
```
