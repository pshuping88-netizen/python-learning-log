#List & Dict Structured Calculation

nums = [{"First Num":"12","Second Num":"74"},{"First Num":"8","Second Num":"93"},{"First Num":"34","Second Num":"67"}]

for num in nums:
    answer = int(num["First Num"]) * int(num["Second Num"])
    print(answer)

#Drill (structured calc)
employees = [{"Name":"KB","Hourly_rate":"200","Hours_worked":"9"},{"Name":"Aiden","Hourly_rate":"76","Hours_worked":"7"}, {"Name":"Joshua","Hourly_rate":"167","Hours_worked":"11"},{"Name":"Shawn","Hourly_rate":"110","Hours_worked":"4"}, {"Name":"Rorisang","Hourly_rate":"80","Hours_worked":"6"}]

#intializing
highest_earn = 0
tot_pay = 0

for employee in employees:
    salary = int(employee["Hourly_rate"]) * int(employee["Hours_worked"])
    print(f"Name: {employee['Name']} Salary: {salary}")
    tot_pay = tot_pay + salary
    if salary > highest_earn:
        highest_earn = salary
        highest_earner = employee["Name"]

print(f"Total Payroll: {tot_pay}\n Highest Earner: {highest_earner} Salary: {highest_earn}")

#Next Drill (structured calc)
app_data = [{"App Name":"Tinder","Usage Hours":"3"},{"App Name":"YouTube","Usage Hours":"12"},{"App Name":"Tiktok","Usage Hours":"5"}]

#initializing
total_hrs = 0
most_hrs = 0

for app in app_data:
    total_hrs = total_hrs + int(app["Usage Hours"])
    if int(app["Usage Hours"]) > most_hrs:
        most_hrs = int(app["Usage Hours"])
        most_used = app["App Name"]
    if int(app["Usage Hours"]) > 3:
        print(f"{app['App Name']} Hours: {app['Usage Hours']}")

print(f"Most used app: {most_used} Most hours: {most_hrs}")