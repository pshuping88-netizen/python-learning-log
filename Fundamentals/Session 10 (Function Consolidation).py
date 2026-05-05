#Functions
#Warm Up

def square(num1):
    return num1*num1

def double(num1):
    return square(num1)

#Core Drill
#Functions
#Employee System V3

#Data
employees = [{"Name":"KB","Hourly_rate":200.00,"Hours_worked":9},{"Name":"Aiden","Hourly_rate":126.00,"Hours_worked":7}, {"Name":"Joshua","Hourly_rate":167.00,"Hours_worked":11},{"Name":"Shawn","Hourly_rate":110.00,"Hours_worked":4}, {"Name":"Rorisang","Hourly_rate":80.00,"Hours_worked":6}]

#Functions
def calculate_salary(rate,hours): #Pure Logic Function
    salary = rate * hours
    return salary

def evaluate_employee(employee): #Transformation Function
    employee_sal = calculate_salary(employee["Hourly_rate"],employee["Hours_worked"])
    return employee["Name"], employee_sal

def process_all_employees(employees): #System Controller Function
    highest_sal = 0
    total_payroll = 0
    for employee in employees:
        employee_sal = evaluate_employee(employee)
        print(f"Name: {employee_sal[0]} Salary: R{employee_sal[1]}")
        total_payroll = total_payroll + employee_sal[1]
        if employee_sal[1] > highest_sal:
            highest_sal = employee_sal[1]
            top_earner = employee_sal[0]
    return total_payroll,top_earner,highest_sal

print(f"----- EMPLOYEE PAYROLL -----")

#Main
total_payroll = process_all_employees(employees)
print(f"Highest Earner: {total_payroll[1]} Salary: {total_payroll[2]} \nTotal Payroll: {total_payroll[0]}")