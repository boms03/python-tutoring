employee_data = [('John', 'Engineering', 75000),('Sarah', 'Marketing', 65000),
                 ('Mike', 'Engineering', 80000),('Lisa', 'Sales', 55000),
                 ('David', 'Marketing', 70000),('Emma', 'Sales', 60000),
                 ('Tom', 'Engineering', 85000)]

'''
1.Find the total salary budget for each department  ( use sum() )
Engineering --> John, Mike, Tom          Marketing --> David, Sarah         Sales --> Lisa, Emma
            75,000 + 80,000 + 85,000        70,000 + 65,000                   55,000 + 60,000


Budget = {i[1] for i in employee_data} ---> Engineering/Marketing/Sales
{for t in {i[1] for i in employee_data}} ---> looping through employee_data, i[1]
{for h in employee_data if t==h[1]} ---> if when looping through it again, if tand h are equal
'''
Budget={t:sum(h[2]for h in employee_data if t==h[1])for t in {i[1] for i in employee_data}}
print(Budget)


'''
2.Count how many employees are in each department  ( use sum() ) —> counting people=+1

Engineering --> John, Mike, Tom (3 people)
Marketing --> David, Sarah (2 people)
Sales --> Lisa, Emma (2 people)

Employees = {i[1] for i in employee_data} --> Engineering/Market/Sales
{for t in {i[1] for i in employee_data}} ---> looping through the departments
{t:sum( for h in employee_data if t==h[1])} --> department: if h and t, when looping                                           both have the same department, +1 to each department.
'''

Employees = {t:sum(1 for h in employee_data if t==h[1])for t in{i[1] for i in employee_data}}
print(Employees)



'''
3. Find the average salary per department ( use 1 and 2 )

Engineering--->total=24,000 %(divided by) 3 (number of people)    = 8,000
Marketing-->total=135,000 %(divided by) 2 (number of people)      = 67,500
Sales--->total=115,000 %(divided by) 2(number of people)          = 57,500

{t:sum(0+1 for h in employee_data if t==h[1])for t in{i[1] for i in employee_data}}
---->  number of employees in each department
{t:sum(h[2]for h in employee_data if t==h[1])for t in {i[1] for i in employee_data}}
--->  number of money in each department
'''




Salary={t:sum(h[2] for h in employee_data if t==h[1])/sum(1 for h in employee_data if t==h[1]) for t in {i[1] for i in employee_data}}
print(Salary)




'''
4.Find which department has the highest total max
---> finding highest number between the totals.

115000  135000  240000
=== 240000 highest




High_Max =

find max of all the total of departments ===
'''


Total={t:sum(h[2]for h in employee_data if t==h[1])for t in {i[1] for i in employee_data}}
print(Total)

MaxSalary=max(j for i,j in Total.items())
print(MaxSalary)

MaxSalaryDepartment={k:MaxSalary for k,v in Total.items() if v==MaxSalary}
print(MaxSalaryDepartment)




