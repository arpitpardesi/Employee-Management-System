import mysql.connector


con = mysql.connector.connect(
    host="localhost", user="root", password="Arpit@123", database="employeeManagement")

def check_employee(employee_id):
    # Query to select all rows from the employees table where id matches
    sql = 'SELECT * FROM employees WHERE id=%s'

    # Making cursor buffered to make rowcount method work properly
    cursor = con.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Fetch the first row to check if employee exists
    employee = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # If employee is found, return True, else return False
    return employee is not None


def add_employee():
    Id = input("Enter Employee Id: ")

    # Checking if Employee with given Id already exists
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return

    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")

        # Inserting Employee details into the employees table
        sql = 'INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)'
        data = (Name, Post, Salary)
        cursor = con.cursor()

        try:
            # Executing the SQL Query
            cursor.execute(sql, data)

            # Committing the transaction
            con.commit()
            print("Employee Added Successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        finally:
            # Closing the cursor
            cursor.close()


def remove_employee():
    Id = input("Enter Employee Id: ")

    # Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    else:
        # Query to delete employee from the employees table
        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        cursor = con.cursor()

        try:
            # Executing the SQL Query
            cursor.execute(sql, data)

            # Committing the transaction
            con.commit()
            print("Employee Removed Successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        finally:
            # Closing the cursor
            cursor.close()


def promote_employee():
    Id = input("Enter Employee's Id: ")

    # Checking if Employee with given Id exists
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    else:
        try:
            Amount = float(input("Enter increase in Salary: "))

            # Query to Fetch Salary of Employee with given Id
            sql_select = 'SELECT salary FROM employees WHERE id=%s'
            data = (Id,)
            cursor = con.cursor()

            # Executing the SQL Query
            cursor.execute(sql_select, data)

            # Fetching Salary of Employee with given Id
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount

            # Query to Update Salary of Employee with given Id
            sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
            data_update = (new_salary, Id)

            # Executing the SQL Query to update salary
            cursor.execute(sql_update, data_update)

            # Committing the transaction
            con.commit()
            print("Employee Promoted Successfully")

        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            con.rollback()

        finally:
            # Closing the cursor
            cursor.close()

def display_employees():
    try:
        # Query to select all rows from the employees table
        sql = 'SELECT * FROM employees'
        cursor = con.cursor()

        # Executing the SQL Query
        cursor.execute(sql)

        # Fetching all details of all the Employees
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Closing the cursor
        cursor.close()