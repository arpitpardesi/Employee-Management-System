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