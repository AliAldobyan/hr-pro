from datetime import datetime

class Employee:

    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return datetime.today().year - int(self.employment_year)

    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %d" % (self.name, self.age, self.salary, self.get_working_years())
        

class Manager(Employee):

    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return float(self.bonus_percentage)* float(self.salary)


    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %d, Bonus: %.5f" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

def main():
    # main code here
    employees = []
    managers = []


    print("Welcome to HR Pro 2019")
    while True:

        print("Options:")
        print("\t1. Show Employees\n\t2. Show Managers\n\t3. Add An Employee\n\t4. Add A Manager\n\t5. Exit")
        user_input = int(input("\nWhat would you like to do? "))
        print("-----------------")

        if user_input == 5:
            break

        elif user_input == 1:
            print("Employees\n")
            for e in employees:
                print(e)
            print("-----------------")

        elif user_input == 2:
            print("Managers\n")
            for m in managers:
                print(m)
            print("-----------------")

        elif user_input == 3:
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            employment_year = input("Employment Year: ")
            employee = Employee(name,age,salary,employment_year)
            employees.append(employee)
            print("Employee added succesfully\n")

        elif user_input == 4:
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            employment_year = input("Employment Year: ")
            bonus = input("Bonus Percentage: ")
            manager = Manager(name,age,salary,employment_year,bonus)
            managers.append(manager)
            print("Manager added succesfully\n")

        else:
            print("Invalid input")



if __name__ == '__main__':
    main()
