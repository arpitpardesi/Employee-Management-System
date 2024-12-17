import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="Arpit@123", database="employeeManagement")

Id = input("Enter Employee's Id: ")

sql = f'SELECT * FROM employees where id={Id}'
cursor = con.cursor()

# Executing the SQL Query
cursor.execute(sql)
employee = cursor.fetchone()
# Fetching all details of all the Employees

# print('Employee ID | Employee Name | Employee Post | Employee Salary')
print("Employee Name : ", employee[1])
print("Employee Post : ", employee[2])
print("Employee Salary : ", employee[3])
print("------------------------------------")