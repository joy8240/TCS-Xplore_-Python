#################################### Test case - 1 #############################
# Input:

# 5
# Sunita
# Faculty
# 23000
# 2
# Jan
# 4
# March
# 6
# Arun
# Admin
# 30000
# 3
# Feb
# 4
# March
# 12
# June
# 10
# Dipak
# Admin
# 25000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Balen
# HR
# 12000









////soultion by joy:
    
    class Employee:
    def __init__(self, employee_name, designation, salary, overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False
        
class Organization:
    def __init__(self, employee_list):
        self.employee_list = employee_list
        
    def check_overtime_eligibility(self, overTimeThreshold):
        for employee in self.employee_list:
            total_overtime_hours = 0
            for month, hours in employee.overTimeContribution.items():
                total_overtime_hours += hours
            if total_overtime_hours >= overTimeThreshold:
                employee.overTimeStatus = True
    
    def calculate_bonus_amount(self, rate_per_hour):
        total_bonus_amount = 0
        for employee in self.employee_list:
            if employee.overTimeStatus:
                total_overtime_hours = 0
                for month, hours in employee.overTimeContribution.items():
                    total_overtime_hours += hours
                total_bonus_amount += total_overtime_hours * rate_per_hour
        return total_bonus_amount
    
n = int(input().strip())
employee_list = []
for i in range(n):
    employee_name = input().strip()
    designation = input().strip()
    salary = int(input().strip())
    overTimeContribution = {}
    m = int(input().strip())
    for j in range(m):
        month = input().strip()
        hours = int(input().strip())
        overTimeContribution[month.lower()] = hours
    employee = Employee(employee_name, designation, salary, overTimeContribution)
    employee_list.append(employee)
    
organization = Organization(employee_list)
overTimeThreshold = int(input().strip())
rate_per_hour = int(input().strip())

organization.check_overtime_eligibility(overTimeThreshold)

for employee in organization.employee_list:
    print(employee.employee_name, employee.overTimeStatus)

print(organization.calculate_bonus_amount(rate_per_hour))

# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Tarun
# HR
# 78000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# 18
# 100

# Output:

# Sunita False
# Arun True
# Dipak True
# Balen True
# Tarun True
# 8600

#################################### Test case - 2 ###########################

# Input:

# 5
# Sunita
# Faculty
# 23000
# 4
# Jan
# 4
# March
# 6
# apr
# 6
# June
# 3
# Arun
# Admin
# 30000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Dipak
# Admin
# 25000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Balen
# HR
# 12000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# Tarun
# HR
# 78000
# 3
# Jan
# 4
# March
# 6
# apr
# 6
# 30
# 100

# Output:

# Sunita False
# Arun False
# Dipak False
# Balen False
# Tarun False
# 0

class Employee:
    def __init__(self,employee_name,designation,salary,overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False

class Organization(Employee):
    def __init__(self,employee_list):
        self.employee_list = employee_list

    def isEligibleForBonus(self,overTimeThreshold):
        for obj in self.employee_list:
            totalOverTimeHours = 0
            for k,v in obj.overTimeContribution.items():
                totalOverTimeHours = totalOverTimeHours + v
                if totalOverTimeHours >= overTimeThreshold:
                    obj.overTimeStatus = True

    def totalBonusToBePaid(self,ratePerHour):
        total = 0
        for obj in self.employee_list:
            if obj.overTimeStatus:
                for k,v in obj.overTimeContribution.items():
                    total = total + v*ratePerHour
        return total

n = int(input())
obj_list = []
for _ in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    overTimeContribution = {}
    for _ in range(int(input())):
        key = input()
        value = int(input())
        overTimeContribution[key] = value
    obj_list.append(Employee(employee_name,designation,salary,overTimeContribution))

org_obj = Organization(obj_list)
overTimeThreshold = int(input())
ratePerHour = int(input())

org_obj.isEligibleForBonus(overTimeThreshold)
totalBonus = org_obj.totalBonusToBePaid(ratePerHour)
for i in obj_list:
    print(i.employee_name,i.overTimeStatus,sep=" ")
print(totalBonus)
